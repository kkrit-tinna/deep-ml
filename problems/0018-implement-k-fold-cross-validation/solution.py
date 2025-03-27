import numpy as np

def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True, random_seed=None):
    """
    Implement k-fold cross-validation by returning train-test indices.
    """
    # # if indicate shuffle, shuffle X & y before proceeding
    # if shuffle:
    #     # shuffle the entire dataset before splitting
    #     if random_seed is not None:
    #         np.random.seed(random_seed)
    #         np.random.shuffle(X)
    # Optionally shuffle the data
    if shuffle:
        if random_seed is not None:
            np.random.seed(random_seed)
        indices = np.random.permutation(len(X))
        X = X[indices]
        y = y[indices]

    # determine size of fold
    fold_size = len(X)//k

    # collect (train-test pair) for each fold  
    X_y_folds = []
    # for each fold of train-test-slit:
    for i in range(k):
        # find list of indices for each split
        # test_indices = indices of test val between the # of current subset and the next subs