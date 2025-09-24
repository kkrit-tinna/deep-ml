# import numpy as np

# def gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size=1, method='batch'):
# 	m = len(y)
#     weights = np.array(weights)

#     for _ in range(n_iterations):
#         if method == 'stochastic':
#             for j in range(m):
#                 y_pred = np.dot(X[j], weights)
#                 error = y_pred - y[j]
#                 gradient = X[j] * error
#                 weights -= learning_rate * gradient
#         elif method == 'mini_batch':
#             for j in range(0, m, batch_size):
#                 X_batch = X[j: j+batch_size]
#                 y_batch = y[j: j+batch_size]
#                 y_pred = np.dot(X_batch, weights)
#                 error = y_pred - y_batch
#                 gradient = np.dot(X_batch.T, error) / len(X_batch)
#                 weights -= learning_rate * gradient
#         elif method == 'batch':
#             y_pred = np.dot(X, weights)
#             error = y_pred - y
#             gradient = np.dot(