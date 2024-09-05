import torch.nn as nn
from torch.nn import functional as F
import torch

def hfreqWH(self, x, scale):
        assert scale>2
        #print(f'input shape: {x.shape}, min: {x.min()}, max: {x.max()}, mean: {x.mean()}')
        x = torch.fft.fft2(x, norm="ortho")#,norm='forward'
        x = torch.fft.fftshift(x, dim=[-2, -1]) 
        b,c,h,w = x.shape
        x[:,:,h//2-h//scale:h//2+h//scale,w//2-w//scale:w//2+w//scale ] = 0.0
        x = torch.fft.ifftshift(x, dim=[-2, -1])
        x = torch.fft.ifft2(x, norm="ortho")
        x = torch.real(x)
        x = F.relu(x, inplace=True)
        #print(f'output shape: {x.shape}, min: {x.min()}, max: {x.max()}, mean: {x.mean()}')
        #print()
        return x

        ### HFRI
        x = self.hfreqWH(x, 4)
        x = F.conv2d(x, self.weight1, self.bias1, stride=1, padding=0)