import numpy as np

def to_categorical(x, n_col=None):
	# if n_col not given, find max value within x
	if n_col == None:
		n_col = int(np.max(x)) + 1
	# create a m*n matrix filled with 0
	oh_matrix = np.zeros((len(x), n_col))
	# for val at index i in x, fill the corresponding space with 1, row_idx=
    oh_matrix[np.arange(len(x)), x] = 1
    return oh_matrix