def searchMatrix(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    top = 0 
    bot = ROWS - 1
    
    while top <= bot:
        mid = (top + bot) // 2
        
        if target < matrix[mid][0]:
            bot = mid - 1
        elif target > matrix[mid][-1]:
            top = mid + 1
        else:
            break

    if  top > bot:
        return False
    
    row = (top + bot) // 2

    
    left = 0
    right = COLS - 1
    
    while left <= right:
        mid = (left + right) // 2
        if target > matrix[row][mid]:
           left = mid + 1
        elif target < matrix[row][mid]:
            right = mid - 1
        else:
            return True
    
    return False 
    
    
    
matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
target = 61

print(searchMatrix(matrix, target))