def firstCompleteIndex(arr, mat) -> int:
    ROWS = len(mat)
    COLS = len(mat[0])
    
    positions = {}
    
    for i in range(ROWS):
        for j in range(COLS):
            positions[mat[i][j]] = (i, j)
            
    print(positions)
    
    rowMap = {}
    for i in range(ROWS):
        rowMap[i] = 0
        
    
    colMap = {}
    for i in range(COLS):
        colMap[i] = 0
        
    for i in range(len(arr)):
        r, c = positions[arr[i]]
        
        
        # print('r', r)
        # print('c', c)
        
        # print('rowMap', rowMap[r])
        # print('colMap', colMap[c])
        
        rowMap[r] += 1
        colMap[c] += 1
        
        if rowMap[r] == COLS:
            return i
        
        if colMap[c] == ROWS:
            return i
        
        # print('rowMap', rowMap)
        # print('colMap', colMap)
    
    
arr = [2,8,7,4,1,3,5,6,9]
mat = [[3,2,5],[1,4,6],[8,7,9]]

res = firstCompleteIndex(arr, mat)

print(res)