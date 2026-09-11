import numpy as np

def simple_self_attention(X: list[list[float]]) -> list[list[float]]:
    X = np.array(X, dtype=np.float32) # put it in an array
    # calculate attention score as dot product of every token 
    attn_scores = X @ X.T

    # apply softmax row-wise for attention weight
    scores_norm = attn_scores - np.max(attn_scores, axis=1, keepdims=True)
    exp_scores = np.exp(scores_norm)
    attn_weight = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    # compute context vector as inputs matrix multiply attention weight
    Z = attn_weight @ X

    return Z.tolist()

