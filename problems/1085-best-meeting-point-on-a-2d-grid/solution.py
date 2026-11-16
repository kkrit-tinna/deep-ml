# total distance = (sum of row distances) + (sum of column distances)
# construct coordinates using 2d grid
#     The plan:
# Scan the grid and collect the row index and column index of every home.
# If there are no homes, return 0.
# Sort the column list. The row list is already sorted if you scan row by row.
# Take the median of each list.
# Sum each coordinate’s absolute distance to its median, and add the two sums.

def best_meeting_point(grid):
    # grid is a list of lists containing 0s and 1s
    # return the minimum total Manhattan distance as an int
    # helper function: find median & calc distances from each x to median
    def total_dist(xs):
        median = xs[len(xs)//2]
        return sum(abs(x-median) for x in xs)

    rows, cols = [], []

    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == 1:
                rows.append(i)
                cols.append(j)
    
    # edge case: no home
    if not rows:
        return 0
    # sort list to find median (rows already sorted)
    cols.sort()

    return total_dist(rows) + total_dist(cols)

