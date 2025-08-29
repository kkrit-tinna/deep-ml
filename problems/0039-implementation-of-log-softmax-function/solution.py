import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    scores = np.array(scores)
    sum_exp = sum(np.exp(scores))
    probs = np.log(np.exp(scores)/sum_exp)
	return probs