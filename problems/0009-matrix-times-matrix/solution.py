def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    # ensure row(a) = col(b)
    if len(a[0]) != len(b):
        return -1
    # initiate new list for storage
	result = []

    # iterate over row of a 
    for i in range(len(a)):
        row = []
        # iterate over column of b
        for j in range(len(b[0])):
            sum = 0
            # iterate over 
            for k in range(len(b)):
                sum += a[i][k]*b[k][j]
            row.append(sum)
        result.append(row)
    return result