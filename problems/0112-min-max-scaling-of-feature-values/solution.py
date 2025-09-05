def min_max(x: list[int]) -> list[float]:
	min_val = min(x)
	max_val = max(x)
	res = []
	for i in x:
		if min_val != max_val:
			res.append((i - min_val) / (max_val - min_val))
		else:
			res.append(0.0)

	return res