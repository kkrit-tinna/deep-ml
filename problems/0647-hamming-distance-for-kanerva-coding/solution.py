import numpy as np

def hamming_distance_kanerva(state: list, prototypes: list, threshold: int) -> tuple:
    """
    Compute Hamming distances and find active prototypes for Kanerva coding.

    Args:
        state: Binary state vector (list of 0s and 1s).
        prototypes: List of binary prototype vectors.
        threshold: Maximum Hamming distance for a prototype to be active.

    Returns:
        Tuple of (distances, active_indices).
    """
    dist = []
    active = []

    for i, proto in enumerate(prototypes):
        d = 0
        for a, b in zip(state, proto):
            if a != b:
                d += 1
        dist.append(d)
        if d <= threshold:
            active.append(i)
    
    return dist, active