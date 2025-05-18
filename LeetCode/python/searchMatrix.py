
def searchMatrix(matrix, target: int) -> bool:
    
    top = 0
    bot = len(matrix) - 1
    
    while top <= bot:
        mid = (top + bot) // 2
        row = matrix[mid]
        
        if target < row[0]:
            bot = mid - 1
        elif target > row[-1]:
            top = mid + 1
        elif target >= row[0] and target <= row[-1]:
            # do binary search here to find the element'
            l = 0
            r = len(row) - 1
            
            while l <= r:
                m = (l + r) // 2
                if row[m] == target:
                    return True
                elif row[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return False
    
    
    return False
    
    

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

res = searchMatrix(matrix, target)

print(res)