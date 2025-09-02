import numpy as np
from itertools import combinations_with_replacement

def polynomial_features(X, degree):
    n_features = X.shape[1]
    n_samples = X.shape[0]

    # Include bias (constant 1) feature
    combos = [()] + [combo for d in range(1, degree + 1) for combo in combinations_with_replacement(range(n_features), d)]
    features = np.empty((n_samples, len(combos)))
    for i, combo in enumerate(combos):
        if combo == ():
            features[:, i] = 1.0
        else:
            features[:, i] = np.prod(X[:, combo], axis=1)
    # Sort each sample's features from lowest to highest
    return np.sort(features, axis=1)