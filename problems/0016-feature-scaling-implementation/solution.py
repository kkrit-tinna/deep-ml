import numpy as np
def feature_scaling(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Standardization: (x - mean) / std
    standardized = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
    # Min-Max Normalization: (x - min) / (max - min)
    normalized = (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))
    # Round results to 4 decimal places
    return np.round(standardized, 4), np.round(normalized, 4)