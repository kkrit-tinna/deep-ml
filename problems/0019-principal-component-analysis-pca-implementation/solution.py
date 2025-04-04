import numpy as np 
def pca(data: np.ndarray, k: int) -> np.ndarray:
	# Standardize the dataset
	data_standardized = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

	# Compute the covariance matrix
	covariance_matrix = np.cov(data_standardized, rowvar=False)

	# Find eigenvalues and eigenvectors
	eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

	# Sort eigenvalues and corresponding eigenvectors
	sorted_indices = np.argsort(eigenvalues)[::-1]
	sorted_eigenvalues = eigenvalues[sorted_indices]
	sorted_eigenvectors = eigenvectors[:, sorted_indices]

	# Select the top k eigenvectors (principal components)
	principal_components = sorted_eigenvectors[:, :k]

	return principal_components