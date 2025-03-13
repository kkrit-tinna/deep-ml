import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape # m is the number of samples, n is the number of features in the dataset
    theta = np.zeros(n) # initialize weights (theta) to zero
    for _ in range(iterations): # for each iteration:
        y_pred = np.dot(X, theta) # features*coefficients
        error = y_pred - y # find error in each round
        gradient = np.dot(X.T, error) / m # find direction 
        theta -= alpha * gradient # update new weights

    return theta