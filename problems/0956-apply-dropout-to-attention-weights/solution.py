import numpy as np

def attention_dropout(attn_weights, values, dropout_rate, mask):
    attn_weights = np.array(attn_weights, dtype=np.float32)
    values = np.array(values, dtype=np.float32)
    mask = np.array(mask)

    if dropout_rate == 0:
        dropped_weights = attn_weights
    else:
        dropped_weights = (attn_weights * mask) / (1 -  dropout_rate)
    
    Z = dropped_weights @ values

    return Z.tolist()
