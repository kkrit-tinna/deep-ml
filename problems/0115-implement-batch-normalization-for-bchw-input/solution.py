import numpy as np

def batch_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
	N, C, H, W = X.shape
    mean = X.mean(axis=(0, 2, 3), keepdims=True)
    var = X.var(axis=(0, 2, 3), keepdims=True)
    X = (X - mean) / np.sqrt(var + epsilon)

    return gamma[:, None, None] * X + beta[:, None, None]