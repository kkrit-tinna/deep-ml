import numpy as np

# def calculate_correlation_matrix(X, Y=None):
#     if Y == None:
# 	    Y = X
#     # s_X = X - np.mean(X, axis=0) / np.std(X, axis=0)
#     # s_Y = Y - np.mean(Y, axis=0) / np.std(Y, axis=0)
#     # corrs = np.dot(s_X.T, s_Y) / (X.shape[0] -  1)
#     corrs = np.corrcoef(X, Y)
# 	return corrs

def calculate_correlation_matrix(X: np.ndarray, Y: np.ndarray = None) -> np.ndarray:
	if Y is None:
		Y = X
	# Compute the covariance matrix
	covariance_matrix = np.cov(X, Y, rowvar=False)[:X.shape[1], X.shape[1]:]
	# Compute the standard deviations
	std_X = np.std(X, axis=0, ddof=1)
	std_Y = np.std(Y, axis=0, ddof=1)
	# Compute the correlation matrix
	correlation_matrix = covariance_matrix / np.outer(std_X, std_Y)
	return correlation_matrix