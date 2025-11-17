import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True, seed=42):
	np.random.seed(seed)
    subsets = []
    n_sample = X.shape[0]

    size = n_sample if replacements else max(1, n_sample // 2)
    for _ in range(n_subsets):
        indices = np.random.choice(n_sample, size=size, replace=replacements)

        X_subset = X[indices].tolist()
        y_subset = y[indices].tolist()
        subsets.append(X_subset)
        subsets.append(y_subset)

    return subsets