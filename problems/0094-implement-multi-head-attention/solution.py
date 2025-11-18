import numpy as np


def compute_qkv(X, W_q, W_k, W_v):
    Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)

    return Q, K, V

def self_attention(Q, K, V):
	d_k = Q.shape[1]
    scores = np.dot(Q, K.T) / np.sqrt(d_k)
    exp_scores = np.exp(scores - np.max(scores, axis=1, keepdims=1))
    attn_weights = exp_scores / np.sum(exp_scores, axis=1, keepdims=1)
    output = np.dot(attn_weights, V)

    return output

def multi_head_attention(Q, K, V, n_heads):
    d_k = Q.shape[1] // n_heads
    d_v = V.shape[1] // n_heads
    heads = []

    for i in range(n_heads):
        Q_i = Q[:, i * d_k:(i + 1) * d_k]
        K_i = K[:, i * d_k:(i + 1) * d_k]
        V_i = V[:, i * d_k:(i + 1) * d_v]

        head = self_attention(Q_i, K_i, V_i)
        heads.append(head)

    return np.concatenate(heads, axis=1).tolist()