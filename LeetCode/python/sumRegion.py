def sumRegion(matrix, row1: int, col1: int, row2: int, col2: int) -> int:
    m = len(matrix)
    n = len(matrix[0])
    
    # for mat in matrix:
    #     print(mat)
        
    # print('------')
    
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0: continue

            if i == 0:
                matrix[i][j] += matrix[i][j-1]
                continue
            if j == 0:
                matrix[i][j] += matrix[i-1][j] 
                continue
            
            matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
            
    
    

        
    if row1 == 0 and col1 == 0:
        return matrix[row2][col2]
    
    if row1 == 0:
        return matrix[row2][col2] - matrix[row2][col1-1] 
    
    if col1 == 0:
        return matrix[row2][col2] - matrix[row1-1][col2] 
    
    # res = 0
    # print(matrix[row2][col2])
    # print(matrix[row1-1][col2])
    # print(matrix[row2][col1-1])
    
    return matrix[row2][col2] - matrix[row1-1][col2] - matrix[row2][col1-1] + matrix[row1-1][col1-1]
        
    
    

matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
sumRegion(matrix, 2, 1, 4, 3)