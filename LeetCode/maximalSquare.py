def maximalSquare(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    maxArea = 0
    
    for i in range(ROWS):
        for j in range(COLS):
            matrix[i][j] = 1 if matrix[i][j] == '1' else 0
    
    for i in range(1, ROWS):
        for j in range(1, COLS):
            if matrix[i][j] == 0:
                continue
            
            # matrix[i][j] != 0 now
            top = matrix[i-1][j]
            left = matrix[i][j-1]
            topLeft = matrix[i-1][j-1]

            if min(top, left, topLeft) == 0:
                continue
            
            matrix[i][j] += min(top, left, topLeft)

    for i in range(ROWS):
        for j in range(COLS):
            maxArea = max(maxArea, matrix[i][j])

    # for p in matrix:
    #     print(p)
    
    return maxArea * maxArea
    


matrix = [["0","1"],["1","0"]]
print(maximalSquare(matrix))
            
