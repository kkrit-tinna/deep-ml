import numpy as np

def l1_regularization_gradient_descent(X: np.array, y: np.array, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
    n_samples, n_features = X.shape

    weights = np.zeros(n_features)
    bias = 0
    
    for _ in range(max_iter):
        y_pred = np.dot(X, weights) + bias
        error = y - y_pred

        grad_w = (-1 / n_samples) * np.dot(X.T, error)
        grad_b = (-1 / n_samples) * np.sum(error)  

        l1_grad = alpha * np.sign(weights)

        weight_grad = grad_w + l1_grad
        bias_grad = grad_b

        new_weights = weights - learning_rate * weight_grad
        new_bias = bias - learning_rate * bias_grad

        # if np.linalg.norm(new_weights - weights) < tol and abs(new_bias - bias) < tol:
        #     break
        
        weights = new_weights
        bias = new_bias

    return weights, bias