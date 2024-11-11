import torch
from torch import nn
from networks.resnet import resnet50
from networks.srm_conv import SRMConv2d_simple
from networks.x_attn import CrossAttention
import torch.nn.functional as F


class PF_CAM(nn.Module):
    def __init__(self, opt, pretrain=True):
        super().__init__()
        self.cam = CrossAttention(num_channels=3, num_heads=1)
        self.srm = SRMConv2d_simple()
        self.disc = resnet50(pretrained=True)
        self.disc.fc = nn.Linear(2048, 1)

    def forward(self, x_b, x_f, x_p):
        x_f_p = self.cam(x_f, x_p)
        x_b_p = self.cam(x_b, x_p)
        x_f_p = F.interpolate(x_f_p, (256, 256), mode='bilinear')
        x_b_p = F.interpolate(x_b_p, (256, 256), mode='bilinear')
        x = torch.cat((x_f_p, x_b_p), dim=1)
        conv = nn.Conv2d(6, 3, kernel_size=1).to(x.device)
        x = conv(x)
        x = self.srm(x)
        x = self.disc(x)
        return x


if __name__ == '__main__':
    model = PF_CAM(pretrain=True)
    print(model)
