import torch
import torch.nn.functional as F

def conv2d_via_unfold(x, W, b, stride=1, padding=0):
    N, C_in, H, W_in = x.shape
    C_out, _, kH, kW = W.shape

    H_out = (H + 2 * padding - kH) // stride + 1
    W_out = (W_in + 2 * padding - kW) // stride + 1

    cols = F.unfold(x, kernel_size=(kH, kW), stride=stride, padding=padding)  # (N, C_in*kH*kW, L)
    W_flat = W.reshape(C_out, -1)  # (C_out, C_in*kH*kW)
    out = W_flat @ cols  # (N, C_out, L)
    out = out.reshape(N, C_out, H_out, W_out)
    return out + b.view(1, C_out, 1, 1)

