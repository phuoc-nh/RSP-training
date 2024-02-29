def minFallingPathSum(matrix):
    n = len(matrix)
    MAX = inf
    for i in range(1,n):
        for j in range(n):
            a = matrix[i-1][j-1] if j - 1 >= 0 else MAX
            b = matrix[i-1][j]
            c = matrix[i-1][j+1] if j + 1 < n else MAX
            matrix[i][j] += min(a, b, c)
            
    print(matrix)
    
    return min(matrix[n-1])
    
matrix = [[-19,57],[-40,-5]]
print(minFallingPathSum(matrix))