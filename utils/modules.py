import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn

def get_device(gpu_ind):
    if torch.cuda.is_available():
        print('Let us use GPU.')
        cudnn.benchmark = True
        if torch.cuda.device_count() == 1:
            device = torch.device('cuda')
        else:
            device = torch.device('cuda:%d' % gpu_ind)
    else:
        print('Come on !! No GPU ?? Who gives you the courage to study Deep Learning ?')
        device = torch.device('cpu')

    return device


class Conv2d(nn.Module):
    def __init__(self, in_channels, out_channels, ksize, padding=0, stride=1, dilation=1, leakyReLU=False):
        super(Conv2d, self).__init__()
        self.convs = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, ksize, stride=stride, padding=padding, dilation=dilation),
            nn.BatchNorm2d(out_channels),
            nn.LeakyReLU(0.1, inplace=True) if leakyReLU else nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.convs(x)