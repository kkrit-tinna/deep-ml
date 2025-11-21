import numpy as np
import math
def pos_encoding(position: int, d_model: int):
	if position == 0 or d_model <= 0:
        return -1
    pos_encodings = np.zeros((position, d_model))
    for i in range(position):
        for j in range(d_model):
            if j % 2 == 0:
                pos_encodings[i, j] = math.sin(i / (10000**(j/d_model)))
            else:
                pos_encodings[i, j] = math.cos(i / (10000**((j - 1)/d_model)))
	pos_encodings = np.float16(pos_encodings)
	return pos_encodings