import numpy as np

def layer_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
	"""
	Perform Layer Normalization.
	"""
	mean = np.mean(X, axis=-1, keepdims=1)
    var = np.var(X, axis=-1, keepdims=True)

    X_normalized = (X - mean) / np.sqrt(var + epsilon)

    output = gamma * X_normalized + beta
	
    return output