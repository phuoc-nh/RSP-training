def spiralOrder(matrix):
    
    rows = len(matrix) 
    cols = len(matrix[0])
    
    top = 0
    left = 0
    
    bottom = rows 
    right = cols
    
    res = []
    while top < bottom and left < right:
        # print('top', top)
        # print('bottom', bottom)
        # print('left', left)
        # print('right', right)
        
        for i in range(left, right):
            res.append(matrix[top][i])
        
        top += 1
        
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        
        right -= 1
        
        if not (left < right and top < bottom):
            break
        
        for i in range(right-1, left - 1, -1):
            res.append(matrix[bottom-1][i])
        
        bottom -= 1
        
        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1
        
        # print('=====')
    # print('res', res)
    
    return res
    
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]
spiralOrder(matrix)