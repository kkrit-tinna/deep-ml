from collections import Counter
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    counts = Counter(samples)

    total_cnt = sum(counts.values())

    if total_cnt == 0:
        return []

    res = []
    for v, c in sorted(counts.items()):
        res.append((v, c/total_cnt))
    return res