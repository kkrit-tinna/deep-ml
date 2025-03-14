import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# convert X & y to array
	X = np.array(X)
	y = np.array(y)
	#
	X_transpose = X.T
	X_transpose_X = np.dot(X_transpose, X)
	X_transpose_y = np.dot(X_transpose, y)

	theta = np.linalg.solve(X_transpose_X, X_transpose_y)
	return theta