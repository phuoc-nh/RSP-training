def numSubmatrixSumTarget(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    for i in range(ROWS):
        for j in range(COLS):
            # cur cell equal top + left - topleft
            top = 0 if i == 0 else matrix[i-1][j]
            left = 0 if j == 0 else matrix[i][j-1]
            topleft = matrix[i-1][j-1] if i > 0 and j > 0 else 0
            print(top, left, topleft)
            
            matrix[i][j] += top + left - topleft
    
    print(matrix)
    res = 0
    for r1 in range(ROWS):
        for r2 in range(r1, ROWS):
            for c1 in range(COLS):
                for c2 in range(c1, COLS):
                    top = 0 if r1 == 0 else matrix[r1-1][c2]
                    left = 0 if c1 == 0 else matrix[r2][c1 - 1]
                    topleft = matrix[r1-1][c1-1] if r1 > 0 and c1 > 0 else 0
                    
                    total = matrix[r2][c2] - (top + left - topleft)
                    if total == target:
                        res += 1
    print(res)
    return res
matrix = [
    [0,1,0],
    [1,1,1],
    [0,1,0]]
target = 0

numSubmatrixSumTarget(matrix, target)


