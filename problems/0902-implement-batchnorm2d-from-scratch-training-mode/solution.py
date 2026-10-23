import torch

def batchnorm2d(x, gamma, beta, eps=1e-5):
    mean = x.mean(dim=(0,2,3), keepdim=True)
    var = x.var(dim=(0,2,3), unbiased=False, keepdim=True)
    x_hat = (x - mean) / torch.sqrt(var + eps)
    return gamma.view(1, -1, 1, 1) * x_hat + beta.view(1, -1, 1, 1)
