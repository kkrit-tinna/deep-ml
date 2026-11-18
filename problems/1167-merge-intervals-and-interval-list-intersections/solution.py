def interval_intervals(intervals):
    # greedy: merge overlapping intervals
    # sort by start first, compare new interval with existing intervals, then merge those whose start <= existing end, else append interval to the list
    merged = []

    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    return merged

def interval_intersections(A, B):
    # merge interval within each list first
    # then use two-pointer to iterate each list to check overlap IF max start <= min end
    A = interval_intervals(A)
    B = interval_intervals(B)
    res = []
    i = j = 0
    while i < len(A) and j < len(B):
        late_start = max(A[i][0], B[j][0])
        early_end = min(A[i][1], B[j][1])
        if late_start <= early_end:
            res.append([late_start, early_end])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return res