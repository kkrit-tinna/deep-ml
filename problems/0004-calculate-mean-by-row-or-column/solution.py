def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == 'row':
		for vector in matrix:
			means.append(sum(vector)/len(vector))
	if mode == 'column':
		for i in range(len(matrix[0])):
			mean = 0
			for j in range(len(matrix)):
				mean += matrix[j][i]
			means.append(mean/len(matrix))
	return means