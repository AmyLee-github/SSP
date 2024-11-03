import torch
from torch import nn
from networks.resnet import resnet50
from networks.srm_conv import SRMConv2d_simple
from networks.se_attn import SE_Net
# from networks.cam import CAM # 不带self-attention
# from networks.transformer_cam import CAM # 带self-attention
import torch.nn.functional as F


class PF_CAM(nn.Module):
    def __init__(self):
        super().__init__()
        # self.cam = CAM(img_size, vit_patch_size, part_out, depth_self, depth_cross, n_heads, mlp_ratio, qkv_bias, p, attn_p)
        self.se_net = SE_Net()
        self.srm = SRMConv2d_simple()
        self.disc = resnet50(pretrained=True)
        self.disc.fc = nn.Linear(2048, 1)

    def forward(self, x_p1, x_f1, x_b1, x_p2, x_f2, x_b2, x_p3, x_f3, x_b3):
        # x = self.cam(x_f, x_p)
        # x = F.interpolate(x, (256, 256), mode='bilinear')
        # patch块与频域块、LBP块concat
        x_f1 = x_f1[:, :1, :, :]
        x_b1 = x_b1[:, :1, :, :]
        x_f2 = x_f2[:, :1, :, :]
        x_b2 = x_b2[:, :1, :, :]
        x_f3 = x_f3[:, :1, :, :]
        x_b3 = x_b3[:, :1, :, :]
        x_pfb1 = torch.cat((x_p1, x_f1, x_b1), dim=1)
        x_pfb2 = torch.cat((x_p2, x_f2, x_b2), dim=1)
        x_pfb3 = torch.cat((x_p3, x_f3, x_b3), dim=1)
        # Assuming SE_Net is defined and imported
        conv = nn.Conv2d(5, 3, kernel_size=1).to(x_pfb1.device)
        x1 = conv(x_pfb1)
        x1 = self.srm(x1)
        x1 = self.disc(x1)
        x2 = conv(x_pfb2)
        x2 = self.srm(x2)
        x2 = self.disc(x2)
        x3 = conv(x_pfb3)
        x3 = self.srm(x3)
        x3 = self.disc(x3)
        x = (x1 + x2 + x3) / 3
        return x


if __name__ == '__main__':
    model = PF_CAM(pretrain=True)
    print(model)
