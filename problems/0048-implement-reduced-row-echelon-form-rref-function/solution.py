import numpy as np

def rref(matrix):
	mat = np.array(matrix, dtype=float) # need to cast float
    rows, cols = mat.shape

	# Perform Gaussian elimination using column-wise pivoting and a separate row pointer
	row = 0
	for c in range(cols):
		if row >= rows:
			break

		# Find pivot in column c at or below the current row
		pivot = np.argmax(np.abs(mat[row:, c])) + row
		if np.isclose(mat[pivot, c], 0.0):
			# No pivot in this column
			continue

		# Swap rows to move pivot into place
		mat[[row, pivot]] = mat[[pivot, row]]

		# Normalize pivot row
		mat[row] = mat[row] / mat[row, c]

		# Eliminate all other entries in this column
		for r in range(rows):
			if r != row:
				mat[r] -= mat[r, c] * mat[row]

		row += 1


    mat[np.isclose(mat, 0.0, atol=1e-12)] = 0.0

    return np.round(mat, 4).tolist()

