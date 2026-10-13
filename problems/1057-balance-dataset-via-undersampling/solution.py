from collections import Counter
def balance_undersample(data: list) -> list:
    """
    Undersample the majority classes so all classes have the same number of
    samples equal to the minority class count.

    data: list of (sample, label) tuples
    Returns: list of (sample, label) tuples, order-preserving
    """
    # corner case: no data
    if not data:
        return []
    
    # initiate a counter and map label: count as key-value pair
    counts = Counter(label for _, label in data)
    # find the min_counts of the data
    min_counts = min(counts.values())

    # iterate (sample, label) in original data, if counts of one label exceeds min counts, omit the rest of the sample
    # initiate a new counter to track # of samples per label (the original order)
    kept_counts = Counter()
    # initiate result list for samples to keep after undersampling
    res = []
    for sample, label in data:
        if kept_counts[label] < min_counts:
            res.append((sample, label))
            kept_counts[label] += 1
    return res


    

