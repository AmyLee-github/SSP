import torch
from torch import nn
from resnet import resnet50
from srm_conv import SRMConv2d_simple
from vit import VisionTransformer
import torch.nn.functional as F
from transformer_cam import cross_encoder


class PFViT(nn.Module):
    def __init__(self,img_size,patch_size, part_out, depth_self, depth_cross, n_heads=16, mlp_ratio=4., qkv_bias=True, p=0., attn_p=0., pretrain=True):
        super().__init__()
        # self.vit = VisionTransformer(
        #     image_size=256,
        #     patch_size=32,
        #     num_classes=1000,
        #     dim=1024,
        #     depth=6,
        #     heads=16,
        #     mlp_dim=2048,
        #     dropout=0.1,
        #     emb_dropout=0.1
        # )
        self.img_size=img_size
        self.patch_size=patch_size
        self.embed_dim=part_out * patch_size * patch_size
        self.num_patches = int(img_size / patch_size) * int(img_size / patch_size)
        self.depth_self=depth_self
        self.depth_cross=depth_cross
        self.cam=cross_encoder(self.img_size, self.patch_size, self.embed_dim, self.num_patches, self.depth_self, self.depth_cross, n_heads=16, mlp_ratio=4., qkv_bias=True, p=0., attn_p=0.)
        self.srm = SRMConv2d_simple()
        self.disc = resnet50(pretrained=True)
        self.disc.fc = nn.Linear(2048, 1)

    def forward(self, x1,x2):
        # x = F.interpolate(x, (256, 256), mode='bilinear')
        x = self.cam(x1,x2)
        x = F.interpolate(x, (256, 256), mode='bilinear')
        # x = self.vit(x)
        x = self.srm(x)
        x = self.disc(x)
        return x


if __name__ == '__main__':
    model = PFViT(pretrain=True)
    print(model)
