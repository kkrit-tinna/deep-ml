import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	# find linear combination of each input
	linear_combo = np.dot(X, weights) + bias
	# apply sigmoid func for probabilistic outcomes
	probs = np.array(list(map(lambda x: 1/(1+np.exp(-x)), linear_combo)))
	# convert probability to 0 or 1 given threshold = 0.5
	predictions = np.where(probs >= 0.5, 1, 0)

	return predictions