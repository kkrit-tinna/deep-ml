from collections import Counter
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
    class_labels, counts = np.unique(y, return_counts=True)
    total = len(y)
    gini = 1.0
    for count in counts:
        prob = count / total
        gini -= prob ** 2
    return round(gini, 3)