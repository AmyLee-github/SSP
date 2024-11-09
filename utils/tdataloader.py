from torch.utils.data import Dataset, DataLoader
import torch
from torch.nn import functional as F
from torchvision import transforms
import os
# from utils.patch import patch_img
from PIL import Image
import numpy as np
import cv2
import random as rd
from random import random, choice
from scipy.ndimage.filters import gaussian_filter
from io import BytesIO
mp = {0: 'imagenet_ai_0508_adm', 1: 'imagenet_ai_0419_biggan', 2: 'imagenet_glide', 3: 'imagenet_midjourney',
      4: 'imagenet_ai_0419_sdv4', 5: 'imagenet_ai_0424_sdv5', 6: 'imagenet_ai_0419_vqdm', 7: 'imagenet_ai_0424_wukong',
      8: 'imagenet_DALLE2'
      }


def sample_continuous(s):
    if len(s) == 1:
        return s[0]
    if len(s) == 2:
        rg = s[1] - s[0]
        return random() * rg + s[0]
    raise ValueError("Length of iterable s should be 1 or 2.")


def sample_discrete(s):
    if len(s) == 1:
        return s[0]
    return choice(s)


def sample_randint(s):
    if len(s) == 1:
        return s[0]
    return rd.randint(s[0], s[1])


def gaussian_blur_gray(img, sigma):
    if len(img.shape) == 3:
        img_blur = np.zeros_like(img)
        for i in range(img.shape[2]):
            img_blur[:, :, i] = gaussian_filter(img[:, :, i], sigma=sigma)
    else:
        img_blur = gaussian_filter(img, sigma=sigma)
    return img_blur


def gaussian_blur(img, sigma):
    gaussian_filter(img[:, :, 0], output=img[:, :, 0], sigma=sigma)
    gaussian_filter(img[:, :, 1], output=img[:, :, 1], sigma=sigma)
    gaussian_filter(img[:, :, 2], output=img[:, :, 2], sigma=sigma)


def cv2_jpg(img, compress_val):
    img_cv2 = img[:, :, ::-1]
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), compress_val]
    result, encimg = cv2.imencode('.jpg', img_cv2, encode_param)
    decimg = cv2.imdecode(encimg, 1)
    return decimg[:, :, ::-1]


def pil_jpg(img, compress_val):
    out = BytesIO()
    img = Image.fromarray(img)
    img.save(out, format='jpeg', quality=compress_val)
    img = Image.open(out)
    # load from memory before ByteIO closes
    img = np.array(img)
    out.close()
    return img


jpeg_dict = {'cv2': cv2_jpg, 'pil': pil_jpg}


def jpeg_from_key(img, compress_val, key):
    method = jpeg_dict[key]
    return method(img, compress_val)


def data_augment(img, opt):
    img = np.array(img)

    if random() < opt.blur_prob:
        sig = sample_continuous(opt.blur_sig)
        gaussian_blur(img, sig)

    if random() < opt.jpg_prob:
        method = sample_discrete(opt.jpg_method)
        qual = sample_randint(opt.jpg_qual)
        img = jpeg_from_key(img, qual, method)

    return Image.fromarray(img)

def compute(patch):
    weight, height = patch[0].size
    m = weight
    res = 0
    patch_np = np.array(patch[0]).astype(np.int64)
    diff_horizontal = np.sum(np.abs(patch_np[:, :-1, :] - patch_np[:, 1:, :]))
    diff_vertical = np.sum(np.abs(patch_np[:-1, :, :] - patch_np[1:, :, :]))
    diff_diagonal = np.sum(np.abs(patch_np[:-1, :-1, :] - patch_np[1:, 1:, :]))
    diff_diagonal += np.sum(np.abs(patch_np[1:, :-1, :] - patch_np[:-1, 1:, :]))
    res = diff_horizontal + diff_vertical + diff_diagonal
    return res.sum()


def patch_img(img, img_f, patch_size, height):
    img_width, img_height = img.size
    height = int(height)
    patch_size = int(patch_size)
    num_patch = (height // patch_size) * (height // patch_size)
    patch_list = []
    min_len = min(img_height, img_width)
    rz = transforms.Resize((height, height))
    if min_len < patch_size:
        img = rz(img)
        img_f = rz(img_f)
    rp = transforms.RandomCrop(patch_size)
    # 随机生成num_patch个不重复随机种子
    seeds = np.random.choice(100000, num_patch, replace=False)
    for i in range(num_patch):
        seed = seeds[i]
        torch.random.manual_seed(seed)
        rp_img = rp(img)
        torch.random.manual_seed(seed)
        rp_img_f = rp(img_f)
        patch_list.append([rp_img, rp_img_f])
    patch_list.sort(key=lambda x: compute(x), reverse=False)
    new_img1, new_img_f1 = patch_list[0][0], patch_list[0][1]
    new_img2, new_img_f2 = patch_list[1][0], patch_list[1][1]
    new_img3, new_img_f3 = patch_list[2][0], patch_list[2][1]
    new_img4, new_img_f4 = patch_list[3][0], patch_list[3][1]

    new_img = Image.new('RGB', (patch_size * 2, patch_size * 2))
    new_img_f = Image.new('RGB', (patch_size * 2, patch_size * 2))

    new_img.paste(new_img1, (0, 0))
    new_img.paste(new_img2, (patch_size, 0))
    new_img.paste(new_img3, (0, patch_size))
    new_img.paste(new_img4, (patch_size, patch_size))

    new_img_f.paste(new_img_f1, (0, 0))
    new_img_f.paste(new_img_f2, (patch_size, 0))
    new_img_f.paste(new_img_f3, (0, patch_size))
    new_img_f.paste(new_img_f4, (patch_size, patch_size))

    return new_img, new_img_f

def processing(img, img_f, opt):
    if opt.aug:
        aug = transforms.Lambda(
            lambda img: data_augment(img, opt)
        )
    else:
        aug = transforms.Lambda(
            lambda img: img
        )

    img_aug = aug(img)

    if opt.isPatch:
        img_aug_p, img_f_p = patch_img(img_aug, img_f, opt.patch_size, opt.trainsize)
    else:
        img_aug_p = transforms.Resize((256, 256))(img_aug)
        img_f_p = transforms.Resize((256, 256))(img_f)

    trans_tensor = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225]),
    ])

    img_aug_p_tensor = trans_tensor(img_aug_p)
    
    # Check if img_f_p has only one channel
    if img_f_p.mode == 'L':
        img_f_p = img_f_p.convert('RGB')
    
    img_f_p_tensor = trans_tensor(img_f_p)

    """
    trans = transforms.Compose([
        aug,
        patch_func,
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225]),
    ])
    """

    return img_aug_p_tensor, img_f_p_tensor

class genImageTrainDataset(Dataset):
    def __init__(self, image_root, image_f_root, image_dir, opt):
        super().__init__()
        self.opt = opt
        self.image_root = image_root
        self.image_f_root = image_f_root
        self.root = os.path.join(image_root, image_dir, "train")
        self.nature_path = os.path.join(self.root, "nature")
        self.nature_list = [os.path.join(self.nature_path, f)
                            for f in os.listdir(self.nature_path)]
        self.nature_size = len(self.nature_list)
        self.ai_path = os.path.join(self.root, "ai")
        self.ai_list = [os.path.join(self.ai_path, f)
                        for f in os.listdir(self.ai_path)]
        self.ai_size = len(self.ai_list)
        self.images = self.nature_list + self.ai_list
        self.labels = torch.cat(
            (torch.ones(self.nature_size), torch.zeros(self.ai_size)))

    def rgb_loader(self, path):
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')

    def get_freq_image_path(self, image_path):
        image_path_f = image_path.replace(self.image_root, self.image_f_root)
        image_dir, image_filename = os.path.split(image_path_f)
        image_name, image_ext = os.path.splitext(image_filename)
        freq_image_filename = image_name + "_f" + image_ext
        freq_image_path = os.path.join(image_dir, freq_image_filename)
        return freq_image_path

    def __getitem__(self, index):
        try:
            image = self.rgb_loader(self.images[index])
            image_path = self.images[index]
            freq_image_path = self.get_freq_image_path(image_path)
            image_f = Image.open(freq_image_path)
            label = self.labels[index]
        except:
            new_index = index - 1
            image = self.rgb_loader(
                self.images[max(0, new_index)])
            freq_image_path = self.get_freq_image_path(self.images[max(0,new_index)])
            image_f = Image.open(freq_image_path)
            label = self.labels[max(0, new_index)]
        image, image_f = processing(image, image_f, self.opt)
        return (image, image_f), label

    def __len__(self):
        return self.nature_size + self.ai_size


class genImageValDataset(Dataset):
    def __init__(self, image_root, image_f_root, image_dir, is_real, opt):
        super().__init__()
        self.opt = opt
        self.image_root = image_root
        self.image_f_root = image_f_root
        self.root = os.path.join(image_root, image_dir, "val")
        if is_real:
            self.img_path = os.path.join(self.root, 'nature')
            self.img_list = [os.path.join(self.img_path, f)
                             for f in os.listdir(self.img_path)]
            self.img_len = len(self.img_list)
            self.labels = torch.ones(self.img_len)
        else:
            self.img_path = os.path.join(self.root, 'ai')
            self.img_list = [os.path.join(self.img_path, f)
                             for f in os.listdir(self.img_path)]
            self.img_len = len(self.img_list)
            self.labels = torch.zeros(self.img_len)

    def rgb_loader(self, path):
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')

    def get_freq_image_path(self, image_path):
        image_path_f = image_path.replace(self.image_root, self.image_f_root)
        image_dir, image_filename = os.path.split(image_path_f)
        image_name, image_ext = os.path.splitext(image_filename)
        freq_image_filename = image_name + "_f" + image_ext
        freq_image_path = os.path.join(image_dir, freq_image_filename)
        return freq_image_path

    def __getitem__(self, index):
        image = self.rgb_loader(self.img_list[index])
        image_path = self.img_list[index]
        freq_image_path = self.get_freq_image_path(image_path)
        image_f = Image.open(freq_image_path)
        label = self.labels[index]
        image, image_f = processing(image, image_f, self.opt)
        return (image, image_f), label

    def __len__(self):
        return self.img_len


class genImageTestDataset(Dataset):
    def __init__(self, image_root, image_f_root, image_dir, opt):
        super().__init__()
        self.opt = opt
        self.image_root = image_root
        self.image_f_root = image_f_root
        self.root = os.path.join(image_root, image_dir, "val")
        self.nature_path = os.path.join(self.root, "nature")
        self.nature_list = [os.path.join(self.nature_path, f)
                            for f in os.listdir(self.nature_path)]
        self.nature_size = len(self.nature_list)
        self.ai_path = os.path.join(self.root, "ai")
        self.ai_list = [os.path.join(self.ai_path, f)
                        for f in os.listdir(self.ai_path)]
        self.ai_size = len(self.ai_list)
        self.images = self.nature_list + self.ai_list
        self.labels = torch.cat(
            (torch.ones(self.nature_size), torch.zeros(self.ai_size)))

    def rgb_loader(self, path):
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')

    def __getitem__(self, index):
        try:
            image = self.rgb_loader(self.images[index])
            image_path = self.images[index]
            freq_image_path = self.get_freq_image_path(image_path)
            image_f = Image.open(freq_image_path)
            label = self.labels[index]
        except:
            new_index = index - 1
            image = self.rgb_loader(
                self.images[max(0, new_index)])
            freq_image_path = self.get_freq_image_path(self.images[max(0,new_index)])
            image_f = Image.open(freq_image_path)
            label = self.labels[max(0, new_index)]
        image, image_f = processing(image, image_f, self.opt)
        return (image, image_f), label, self.images[index]

    def __len__(self):
        return self.nature_size + self.ai_size


def get_single_loader(opt, image_dir, is_real):
    val_dataset = genImageValDataset(
        opt.image_root, opt.image_f_root, image_dir=image_dir, is_real=is_real, opt=opt)
    val_loader = DataLoader(val_dataset, batch_size=opt.val_batchsize,
                            shuffle=False, num_workers=4, pin_memory=True)
    return val_loader, len(val_dataset)


def get_val_loader(opt):
    choices = opt.choices
    loader = []
    for i, choice in enumerate(choices):
        datainfo = dict()
        if choice == 0 or choice == 1:
            print("val on:", mp[i])
            datainfo['name'] = mp[i]
            datainfo['val_ai_loader'], datainfo['ai_size'] = get_single_loader(
                opt, datainfo['name'], is_real=False)
            datainfo['val_nature_loader'], datainfo['nature_size'] = get_single_loader(
                opt, datainfo['name'], is_real=True)
            loader.append(datainfo)
    return loader


def get_loader(opt):
    choices = opt.choices
    image_root = opt.image_root
    image_f_root= opt.image_f_root

    datasets = []
    if choices[0] == 1:
        adm_dataset = genImageTrainDataset(
            image_root, image_f_root, "imagenet_ai_0508_adm", opt=opt)
        datasets.append(adm_dataset)
        print("train on: imagenet_ai_0508_adm")
    if choices[1] == 1:
        biggan_dataset = genImageTrainDataset(
            image_root, image_f_root, "imagenet_ai_0419_biggan", opt=opt)
        datasets.append(biggan_dataset)
        print("train on: imagenet_ai_0419_biggan")
    if choices[2] == 1:
        glide_dataset = genImageTrainDataset(
            image_root, image_f_root, "imagenet_glide", opt=opt)
        datasets.append(glide_dataset)
        print("train on: imagenet_glide")
    if choices[3] == 1:
        midjourney_dataset = genImageTrainDataset(
            image_root, image_f_root, "imagenet_midjourney", opt=opt)
        datasets.append(midjourney_dataset)
        print("train on: imagenet_midjourney")
    if choices[4] == 1:
        sdv14_dataset = genImageTrainDataset(
            image_root, image_f_root, "imagenet_ai_0419_sdv4", opt=opt)
        datasets.append(sdv14_dataset)
        print("train on: imagenet_ai_0419_sdv4")
    if choices[5] == 1:
        sdv15_dataset = genImageTrainDataset(
            image_root, image_f_root, "imagenet_ai_0424_sdv5", opt=opt)
        datasets.append(sdv15_dataset)
        print("train on: imagenet_ai_0424_sdv5")
    if choices[6] == 1:
        vqdm_dataset = genImageTrainDataset(
            image_root, image_f_root, "imagenet_ai_0419_vqdm", opt=opt)
        datasets.append(vqdm_dataset)
        print("train on: imagenet_ai_0419_vqdm")
    if choices[7] == 1:
        wukong_dataset = genImageTrainDataset(
            image_root, image_f_root, "imagenet_ai_0424_wukong", opt=opt)
        datasets.append(wukong_dataset)
        print("train on: imagenet_ai_0424_wukong")

    train_dataset = torch.utils.data.ConcatDataset(datasets)
    train_loader = DataLoader(train_dataset, batch_size=opt.batchsize,
                              shuffle=True, num_workers=4, pin_memory=True) #TODO: 这里num_workers改成1试试
    return train_loader


def get_test_loader(opt):
    choices = opt.choices
    image_root = opt.image_root
    image_f_root= opt.image_f_root

    datasets = []
    if choices[0] == 2:
        adm_dataset = genImageTestDataset(
            image_root, image_f_root, "imagenet_ai_0508_adm", opt=opt)
        datasets.append(adm_dataset)
        print("test on: imagenet_ai_0508_adm")
    if choices[1] == 2:
        biggan_dataset = genImageTestDataset(
            image_root, image_f_root, "imagenet_ai_0419_biggan", opt=opt)
        datasets.append(biggan_dataset)
        print("test on: imagenet_ai_0419_biggan")
    if choices[2] == 2:
        glide_dataset = genImageTestDataset(
            image_root, image_f_root, "imagenet_glide", opt=opt)
        datasets.append(glide_dataset)
        print("test on: imagenet_glide")
    if choices[3] == 2:
        midjourney_dataset = genImageTestDataset(
            image_root, image_f_root, "imagenet_midjourney", opt=opt)
        datasets.append(midjourney_dataset)
        print("test on: imagenet_midjourney")
    if choices[4] == 2:
        sdv14_dataset = genImageTestDataset(
            image_root, image_f_root, "imagenet_ai_0419_sdv4", opt=opt)
        datasets.append(sdv14_dataset)
        print("test on: imagenet_ai_0419_sdv4")
    if choices[5] == 2:
        sdv15_dataset = genImageTestDataset(
            image_root, image_f_root, "imagenet_ai_0424_sdv5", opt=opt)
        datasets.append(sdv15_dataset)
        print("test on: imagenet_ai_0424_sdv5")
    if choices[6] == 2:
        vqdm_dataset = genImageTestDataset(
            image_root, image_f_root, "imagenet_ai_0419_vqdm", opt=opt)
        datasets.append(vqdm_dataset)
        print("test on: imagenet_ai_0419_vqdm")
    if choices[7] == 2:
        wukong_dataset = genImageTestDataset(
            image_root, image_f_root, "imagenet_ai_0424_wukong", opt=opt)
        datasets.append(wukong_dataset)
        print("test on: imagenet_ai_0424_wukong")

    test_dataset = torch.utils.data.ConcatDataset(datasets)
    test_loader = DataLoader(test_dataset, batch_size=opt.batchsize,
                             shuffle=True, num_workers=4, pin_memory=True)
    return test_loader