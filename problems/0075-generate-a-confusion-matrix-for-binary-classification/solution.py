import numpy as np

def confusion_matrix(data):
	tp = sum(1 for true, pred in data if true == 1 and pred == 1)
    fp = sum(1 for true, pred in data if true == 0 and pred == 1)
    tn = sum(1 for true, pred in data if true == 0 and pred == 0)
    fn = sum(1 for true, pred in data if true == 1 and pred == 0)

    return [tp, fn], [fp, tn]