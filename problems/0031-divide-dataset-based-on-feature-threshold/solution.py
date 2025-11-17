import numpy as np

def divide_on_feature(X, feature_i, threshold):
	X_left = X[X[:, feature_i] >= threshold]
    X_right = X[X[:, feature_i] < threshold]
    return X_left, X_right