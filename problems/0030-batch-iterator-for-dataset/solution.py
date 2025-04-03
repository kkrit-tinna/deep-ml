import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    # empty list for storage
    new_lst = []
    # if y is not given:
    if y is None:
        for i in range(0, len(X), batch_size):
            new_lst.append(X[i: i+batch_size])
    else:
        for i in range(0, len(X), batch_size):
            new_lst.append([X[i: i+batch_size], y[i: i+batch_size]])

    return new_lst
