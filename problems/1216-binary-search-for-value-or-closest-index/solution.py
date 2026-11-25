def binary_search_closest(arr, target):
    # arr is sorted in non-decreasing order
    # return an integer index (or -1 for empty arr)
    # edge case: empty array
    if not arr:
        return -1
    low, high = 0, len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    # target is exact match 
    # (loop have a few more passes for finding the smallest index if there are duplicates)
    if low < len(arr) and arr[low] == target:
        return low
    # target is not exact match
    # 1)target outside range: smaller than the smallest
    if low == 0:
        return 0
    # 2)target outside range: greater than the greatest
    if low == len(arr):
        return len(arr) - 1
    
    # 3)target inside the range: find index of the closest number, take smaller index IF equally close
    if target - arr[low - 1] <= arr[low] - target:
        return low - 1
    return low