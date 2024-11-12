import torch
from torch import nn
from networks.resnet import resnet50
from networks.srm_conv import SRMConv2d_simple
from networks.x_attn import CrossAttention
import torch.nn.functional as F


class PF_CAM(nn.Module):
    def __init__(self, opt, pretrain=True):
        super().__init__()
        num_heads = opt.n_heads
        self.cam = CrossAttention(num_channels=3, num_heads=1)
        self.srm = SRMConv2d_simple()
        self.disc = resnet50(pretrained=True)
        self.disc.fc = nn.Linear(2048, 1)

    def forward(self, x_b, x_p):
        x = self.cam(x_b, x_p)
        x = F.interpolate(x, (256, 256), mode='bilinear')
        x = self.srm(x)
        x = self.disc(x)
        return x


if __name__ == '__main__':
    model = PF_CAM(pretrain=True)
    print(model)
