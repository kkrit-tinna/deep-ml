def top_three_largest(values):
    # values: list of numbers
    # return the three largest values in descending order
    
    # use vars to keep top-k values --> one scan, no storage

    first = second = third = None
    cnt = 0 # in case less than 3
    for v in values:
        cnt += 1
        if first is None or v > first:
            first, second, third = v, first, second
        elif second is None or v > second:
            second, third = v, second
        elif third is None or v > third:
            third = v
    
    return [first, second, third][:min(3, cnt)]