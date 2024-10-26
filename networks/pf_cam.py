import torch
from torch import nn
from networks.resnet import resnet50
from networks.srm_conv import SRMConv2d_simple
from networks.cam import CAM # 不带self-attention
# from networks.transformer_cam import CAM # 带self-attention
import torch.nn.functional as F


class PF_CAM(nn.Module):
    def __init__(self, img_size, vit_patch_size, part_out, depth_self, depth_cross, n_heads=4, mlp_ratio=4., qkv_bias=True, p=0., attn_p=0., pretrain=True):
        super().__init__()
        # self.cam = CAM(img_size, vit_patch_size, part_out, depth_self, depth_cross, n_heads, mlp_ratio, qkv_bias, p, attn_p)
        self.srm = SRMConv2d_simple()
        self.disc = resnet50(pretrained=True)
        self.disc.fc = nn.Linear(2048, 1)

    def forward(self, x_b, x_f, x_p):
        # x = self.cam(x_f, x_p)
        # x = F.interpolate(x, (256, 256), mode='bilinear')
        # patch块与频域块、LBP块concat
        x_f = x_f[:, :1, :, :]
        x_b = x_b[:, :1, :, :]
        x_b_rz = F.interpolate(x_b, (256, 256), mode='bilinear')
        x_f_rz = F.interpolate(x_f, (256, 256), mode='bilinear')
        x_p_rz = F.interpolate(x_p, (256, 256), mode='bilinear')
        x = torch.cat((x_b_rz, x_f_rz, x_p_rz), dim=1)
        conv = nn.Conv2d(5, 3, kernel_size=1).to(x.device)
        x = conv(x)
        x = self.srm(x)
        x = self.disc(x)
        return x


if __name__ == '__main__':
    model = PF_CAM(pretrain=True)
    print(model)
