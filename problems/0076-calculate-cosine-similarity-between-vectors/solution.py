
import numpy as np

def cosine_similarity(v1, v2):
    if len(v1) != len(v2):
        return -1.0
	dot_prod = np.dot(v1, v2)
    v1_mag = np.linalg.norm(v1)
    v2_mag = np.linalg.norm(v2)
    if v1_mag == 0 or v2_mag == 0:
        return 0.0
    else:
        return round(dot_prod / (v1_mag * v2_mag), 3)

