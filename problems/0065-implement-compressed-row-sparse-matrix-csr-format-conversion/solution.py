import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	vals = []
    col_idxs = []
    row_ptr = [0]

    for row in dense_matrix:
        for col_idx in range(len(row)):
            if row[col_idx] != 0:
                vals.append(row[col_idx])
                col_idxs.append(col_idx)
        row_ptr.append(len(vals))

    return vals, col_idxs, row_ptr
