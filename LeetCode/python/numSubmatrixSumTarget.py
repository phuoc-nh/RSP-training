def numSubmatrixSumTarget(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    prefixSum = [[0 for i in range(COLS)] for j in range(ROWS)]
    m = {0: 1}
    res = 0
    for i in range(ROWS):
        for j in range(COLS):
            top = prefixSum[i-1][j] if i >= 1 else 0
            left = prefixSum[i][j-1] if j >= 1 else 0
            topLeft = prefixSum[i-1][j-1] if min(i,j) >= 1 else 0
            prefixSum[i][j] = matrix[i][j] + top + left - topLeft 
            m[prefixSum[i][j]] = m.get(prefixSum[i][j], 0) + 1
            diff = target - prefixSum[i][j]
            
            res += m.get(diff, 0)
    print(res)
    # for r1 in range(ROWS):
    #     for r2 in range(r1, ROWS):
    #         for c1 in range(COLS):
    #             for c2 in range(c1, COLS):
    #                 top = prefixSum[r1-1][c2] if r1 >= 1 else 0
    #                 left = prefixSum[r2][c1-1] if c1 >= 1 else 0
    #                 topLeft = prefixSum[r1-1][c1-1] if min(r1, c1) >= 1 else 0
    #                 curSum = prefixSum[r2][c2] - top - left + topLeft
    #                 if curSum == target:
    #                     res += 1
    # for p in prefixSum:
        # print(p)
    



    print(res)        
    return res


matrix = [[1,-1],[-1,1]]
target = 0

numSubmatrixSumTarget(matrix, target)


