import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    clipped_probs = np.clip(predicted_probs, epsilon, 1-epsilon)
    losses = -np.sum(true_labels * np.log(clipped_probs), axis=-1)
    return float(np.mean(losses))