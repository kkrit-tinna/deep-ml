def first_n_fibonacci(n):
    # edge case: 0 & 1
    if n <= 0:
        return []
    
    if n == 1:
        return [0]
    
    if n== 2:
        return [0, 1]
    # avoid base case recomputed in recursion
    res = first_n_fibonacci(n-1) 
    res.append(res[-1] + res[-2])

    return res

# avoids using recursion directly because python caps at about 1000 calls, use iteration for large n