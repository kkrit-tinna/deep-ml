import numpy as np
def softmax(scores):
	scores = np.array(scores)
	exp_scores = np.exp(scores - np.max(scores, axis=1, keepdims=True))
	sum_exp = np.sum(exp_scores, axis=1, keepdims=True)
	return exp_scores / sum_exp

def compute_qkv(X, W_q, W_k, W_v):
	Q = np.dot(X, W_q)
	K = np.dot(X, W_k)
	V = np.dot(X, W_v)
	return Q, K, V

def self_attention(Q, K, V):
    d_k = Q.shape[1]
	attention_scores = np.dot(Q, K.T) / np.sqrt(d_k)
	attention_weights = softmax(attention_scores)
	attention_output = np.dot(attention_weights, V)

	return attention_output.tolist()
