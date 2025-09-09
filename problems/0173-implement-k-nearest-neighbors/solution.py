import numpy as np
def k_nearest_neighbors(points, query_point, k):
    """
    Find k nearest neighbors to a query point
    
    Args:
        points: List of tuples representing points [(x1, y1), (x2, y2), ...]
        query_point: Tuple representing query point (x, y)
        k: Number of nearest neighbors to return
    
    Returns:
        List of k nearest neighbor points as tuples
    """
    points = np.array(points)
    query_point = np.array(query_point)

    distances = np.linalg.norm(points - query_point, axis=1)

    top_k_idx = np.argsort(distances)[:k]

    res = []

    for idx in top_k_idx:
        res.append(tuple(points[idx]))

    return res
    