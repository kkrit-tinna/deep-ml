import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    # convert all matrices to numpy matrices
    A = np.array(A)
    T = np.array(T)
    S = np.array(S)
    # check if invertible
    if np.linalg.det(S) == 0 or np.linalg.det(T) == 0:
        return -1
    
    # inverse T
    T_inv = np.linalg.inv(T)

    transformed_matrix = np.dot(np.dot(T_inv, A), S)

	return transformed_matrix