def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    if a*d - b*c == 0:
        return None
    else:
        scalar = 1/(a*d - b*c)
        inverse = [[scalar * d, scalar * (-b)], [scalar * (-c), scalar * a]]
	return inverse