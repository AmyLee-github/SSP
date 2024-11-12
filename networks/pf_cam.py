import torch
from torch import nn
from networks.resnet import resnet50
from networks.srm_conv import SRMConv2d_simple
from networks.x_attn import CrossAttention
from networks.SEAttention import SEAttention
import torch.nn.functional as F


class PF_CAM(nn.Module):
    def __init__(self, pretrain=True):
        super().__init__()
        self.cam1 = CrossAttention(num_channels=3, num_heads=1)
        self.cam3 = CrossAttention(num_channels=3, num_heads=3)
        self.se = SEAttention(channel=6,reduction=2)
        self.srm = SRMConv2d_simple()
        self.disc = resnet50(pretrained=True)
        self.disc.conv1 = nn.Conv2d(6, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.disc.fc = nn.Linear(2048, 1)

    def forward(self, x_b, x_f, x_p):
        x_f_p = self.cam1(x_f, x_p)
        x_b_p = self.cam3(x_b, x_p)
        x = torch.cat((x_f_p, x_b_p), dim=1)
        x = self.se(x)
        x_f_p = x[:, :3, :, :]
        x_b_p = x[:, 3:, :, :]
        x_f_p = F.interpolate(x_f_p, (256, 256), mode='bilinear')
        x_b_p = F.interpolate(x_b_p, (256, 256), mode='bilinear')
        x_f_p = self.srm(x_f_p)
        x_b_p = self.srm(x_b_p)
        x = torch.cat((x_f_p, x_b_p), dim=1)
        x = self.disc(x)
        return x


if __name__ == '__main__':
    x_f = torch.randn(64, 3, 64, 64)
    x_b = torch.randn(64, 3, 64, 64)
    x_p = torch.randn(64, 3, 64, 64)
    model = PF_CAM(pretrain=True)
    output = model(x_b, x_f, x_p)
    print(output.shape)
    print(model)
