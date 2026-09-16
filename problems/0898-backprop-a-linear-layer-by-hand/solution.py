import torch

def linear_backward(grad_output, x, W):
    grad_input = grad_output @ W  # Compute gradient w.r.t. input, (N,out) @ (out,in) = (N,in) 
    grad_weights = grad_output.T @ x # Compute gradient w.r.t. weights, (out,N) @ (N,in) = (out,in) 
    grad_bias = grad_output.sum(dim=0)  # Compute gradient w.r.t. bias, (out,) 
    return grad_input, grad_weights, grad_bias