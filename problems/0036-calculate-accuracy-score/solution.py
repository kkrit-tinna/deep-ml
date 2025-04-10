import numpy as np

def accuracy_score(y_true, y_pred):
    if len(y_true) != len(y_pred):
        return -1
    else:
        corrects = np.sum(y_true == y_pred)
        accuracy = corrects / len(y_true)
	return accuracy