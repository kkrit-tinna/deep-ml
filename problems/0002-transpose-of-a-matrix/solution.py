def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	b = []
	for i in range(len(a[0])):
		c = []
		for j in range(len(a)):
			c.append(a[j][i])
		b.append(c)
	return b