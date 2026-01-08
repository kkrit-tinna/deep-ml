import numpy as np

def group_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, num_groups: int, epsilon: float = 1e-5) -> np.ndarray:
    N, C, H, W = X.shape
    X = X.reshape(N, num_groups, C // num_groups, H, W)
    mean = X.mean(axis=(2, 3, 4), keepdims=True)
    var = X.var(axis=(2, 3, 4), keepdims=True)
    X = (X - mean) / np.sqrt(var + epsilon)
    X = X.reshape(N, C, H, W)

    return gamma[:, None, None] * X + beta[:, None, None]