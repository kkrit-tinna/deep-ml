import numpy as np

def compute_qkv(X: np.ndarray, W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray):
	"""
	Compute Query (Q), Key (K), and Value (V) matrices.
	"""
	return np.dot(X, W_q), np.dot(X, W_k), np.dot(X, W_v)

def masked_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray, mask: np.ndarray) -> np.ndarray:
	"""
	Compute masked self-attention.
	"""
	d_k = Q.shape[1]
	scores = np.dot(Q, K.T) / np.sqrt(d_k)
	
	# Apply mask safely: assume mask marks positions to be masked (True/1).
	# Use np.where so we don't introduce NaNs or infs by arithmetic on non-boolean masks.
	if mask is not None:
		mask_bool = np.asarray(mask, dtype=bool)
		scores = np.where(mask_bool, -1e9, scores)

	# Ensure no NaN/inf values remain before subtracting the row-wise max for numerical stability
	scores = np.nan_to_num(scores, nan=-1e9, posinf=1e9, neginf=-1e9)

	exp_scores = np.exp(scores - np.max(scores, axis=1, keepdims=1))
	attention_weights = exp_scores / np.sum(exp_scores, axis=1, keepdims=1)

	re