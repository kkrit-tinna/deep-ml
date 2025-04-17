import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	
	y_pred = np.dot(X, w)

    mse = np.mean((y_true - y_pred)**2)

    ridge_term = alpha * np.sum(w**2)

    total_loss = mse + ridge_term

    return total_loss
