import numpy as np

# Do not call np.ones, np.full, or np.ones_like. Build the result from np.arange and arithmetic/broadcasting only.
def ones(n: int) -> np.ndarray:
    """Return a length-n float vector of ones without calling np.ones."""
    # Any number times 0 is 0, so this gives n zeros; adding 1 turns them into ones
    return np.arange(n, dtype=np.float64) * 0 + 1

# Implement vector_sum(a) that returns the sum of all elements of a 1-D NumPy array a as a 0-D / scalar NumPy value (e.g. np.float64).
# Do not call np.sum, a.sum(), sum(), or Python loops. Use a dot product with a ones vector (built from np.arange + arithmetic) instead.
def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    a = np.asarray(a, dtype=np.float64)
    # a · 1 = a1*1 + a2*1 + ... + an*1, which is just the sum of a
    return np.dot(a, ones(a.shape[0]))