def find_duplicates(records):
    # records: list of hashable items (ints or strings)
    # return a list of values that appear more than once,
    # each listed once, ordered by the position of its second occurrence
    res = []

    seen = set() # initiate an empty set for seen items
    reported = set() # initiate an empty set for reported item

    for i in records:
        if i in seen:
            if i not in reported:
                reported.add(i)
                res.append(i)
        else:
            seen.add(i)
    
    return res



