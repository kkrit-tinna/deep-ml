from collections import Counter
def count_common_unique(list1, list2):
    # list1: list of strings
    # list2: list of strings
    # return an integer
    c1 = Counter(list1)
    c2 = Counter(list2)

    once1 = {w for w, c in c1.items() if c==1}
    
    once2 = {w for w, c in c2.items() if c==1}
    
    return len(once1 & once2)