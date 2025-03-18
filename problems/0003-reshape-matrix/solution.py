import numpy as np
import math
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	try:
		a_arr = np.array(a)
		result = a_arr.reshape(new_shape).tolist()
		return result
	except ValueError:
		return []
	