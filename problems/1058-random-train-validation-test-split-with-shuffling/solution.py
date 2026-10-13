import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    n = data.shape[0]
    indices = np.random.default_rng(seed).permutation(n)

    train_end = int(n*train_frac)
    validation_end = train_end + int(n * validation_frac)

    train_idx = indices[:train_end]
    validation_idx = indices[train_end:validation_end]
    test_idx = indices[validation_end:]

    return [data[train_idx], data[validation_idx], data[test_idx]]


