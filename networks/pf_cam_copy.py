import torch
from torch import nn
from networks.resnet import resnet50
from networks.srm_conv import SRMConv2d_simple
import torch.nn.functional as F


class PF_CAM(nn.Module):
    def __init__(self):
        super().__init__()
        self.srm = SRMConv2d_simple()
        self.disc = resnet50(pretrained=True)
        self.disc.fc = nn.Linear(2048, 1)

    def forward(self, x_p, x_f, x_b):
        x_pfb = torch.cat((x_p, x_f, x_b), dim=1)
        conv = nn.Conv2d(5, 3, kernel_size=1).to(x_pfb.device)
        x = conv(x_pfb)
        x = self.srm(x)
        x = self.disc(x)
        return x


if __name__ == '__main__':
    model = PF_CAM(pretrain=True)
    print(model)
