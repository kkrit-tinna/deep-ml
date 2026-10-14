import numpy as np

def cross_product(a, b):
    a = np.array(a)
    b = np.array(b)
    if a.shape[0] != 3 or b.shape[0] != 3:
        raise ValueError("Both vectors must be 3-dimensional")
    
    return np.array(
        [a[1]*b[2] - a[2] * b[1],
        a[2]*b[0] - a[0] * b[2],
        a[0]*b[1] - a[1] * b[0]]
    )