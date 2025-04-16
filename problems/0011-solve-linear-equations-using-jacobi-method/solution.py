import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    # find the diagonal of A
    d_a = np.diag(A)
    # find the non-diagonal part of A
    nda = A - np.diag(d_a)
    # initial guesses for x
    x = np.zeros(len(b))
    # initate a hold variable to store the new x values
    x_hold = np.zeros(len(b))
    # iterate n times
    for _ in range(n):
        # iterate through each row of A
        for i in range(len(A)):
            # calculate the new x value for each row
            x_hold[i] = (1/d_a[i]) * (b[i] - sum(nda[i]*x))
        # copy the new x values and round the new x values to 4 decimal places
        x = x_hold.copy()
    return np.round(x,4).tolist()