import numpy as np

def shuffle_data(X, y, seed=None):
	# set seed if given any
	if seed is None:
		seed = np.random.randint(0, 1000)
	# make sure both arrays have the same permutation
	np.random.seed(seed)
	np.random.shuffle(X)
	np.random.seed(seed)
	np.random.shuffle(y)
	return X, y