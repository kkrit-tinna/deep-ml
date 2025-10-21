def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	vals = []
    row_idx = []
    col_ptr = [0]

    for col in range(len(dense_matrix[0])):
        for row in range(len(dense_matrix)):
            if dense_matrix[row][col] != 0:
                vals.append(dense_matrix[row][col])
                row_idx.append(row)
        col_ptr.append(len(vals))

    return vals, row_idx, col_ptr
