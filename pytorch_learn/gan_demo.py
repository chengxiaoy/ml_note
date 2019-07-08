from torch import nn
import torch
import numpy as np
import torchvision
from torch.autograd import Variable


class autoencoder(nn.Module):
    def __init__(self):
        super(autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(28 * 28, 128),
            nn.ReLU(True),
            nn.Linear(128, 64),
            nn.ReLU(True),
            nn.Linear(64, 12),
            nn.ReLU(True),
            nn.Linear(12, 3)
        )

        self.decoder = nn.Sequential(
            nn.Linear(3, 12),
            nn.ReLU(True),
            nn.Linear(12, 64),
            nn.ReLU(True),
            nn.Linear(64, 128),
            nn.ReLU(True),
            nn.Linear(128, 28 * 28),
            nn.Tanh()
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x


reconstruction_function = nn.MSELoss()


def loss_function(recon_x, x, mu, logvar):
    mse = reconstruction_function(recon_x,x)
    kld_element = mu.pow(2).add_(logvar.exp()).mul_(-1 )

torch.Tensor(10).normal_()