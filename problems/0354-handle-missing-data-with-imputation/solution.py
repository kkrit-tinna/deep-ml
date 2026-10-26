import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    # edge case: strategy not known
    if strategy not in ('mean', 'median', 'mode'):
        raise ValueError("Unknown strategy. Please choose from mean, median, mode")
    results = np.array(data, dtype=float)

    # find missing data by column
    for j in range(results.shape[1]):
        col = results[:, j]
        missing = np.isnan(col)
        not_missing = col[~missing]

        # if the entire column is empty, leave as it is 
        if not_missing.size == 0 or not missing.any():
            continue
        
        # decide fill by strategies
        if strategy == 'mean':
            fill = np.mean(not_missing)
        elif strategy == 'median':
            fill = np.median(not_missing)
        else:
            # np.unique returns sorted values, so argmax picks the smallest on ties
            values, counts = np.unique(not_missing, return_counts=True)
            fill = values[np.argmax(counts)]
        
        col[missing] = fill

    return results
