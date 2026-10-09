import numpy as np
from itertools import combinations
def ovr_predict(scores):
    """
    scores: (n_samples, n_classes) decision scores, one column per one-vs-rest classifier.
    Returns: (n_samples,) int array of predicted classes.
    """
    scores = np.asarray(scores)
    return np.argmax(scores, axis=1) # index of max within each sample

def ovo_predict(pair_scores, n_classes):
    """
    pair_scores: (n_samples, n_pairs) decision scores, one column per pair (i, j), i < j,
                 in lexicographic order. Positive votes for j, otherwise for i.
    Returns: (n_samples,) int array of predicted classes (ties -> smallest index).
    """
    pair_scores = np.asarray(pair_scores)
    n_samples = pair_scores.shape[0] # how many samples

    # initate votes in [sample, class] shape, choose which class to vote later
    votes = np.zeros((n_samples, n_classes), dtype=int)

    # construct the pair based on pair_scores
    # MUST PASS IN AN ITER FOR COMBINATIONS TO ITERATE
    # MUST USE LIST() TO FORCE ITERATOR TO ITERATE INSTEAD OF PASS IN AN INTERATE OBJECT: <itertools.combinations object at 0x...>
    pairs = list(combinations(range(n_classes), 2))
    
    # assign vote to each pair
    for col, (i, j) in enumerate(pairs):
        # extract score and check pos/non-pos (bool)
        pos = pair_scores[:, col] > 0
        # if pos, count towards j
        votes[pos, j] += 1
        # if not pos, count toward i
        votes[~pos, i] += 1

    return np.argmax(votes, axis=1)
    
