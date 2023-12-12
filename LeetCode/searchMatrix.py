def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        if binarySearch(matrix[i], target):
            return True
        
    return False    

def binarySearch(arr, target):
    l = 0
    r = len(arr) - 1
    # print(arr)
    while l <= r:
        mid = (r + l) // 2
        # print(mid)
        # print(r, l)
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return False

# matrix = [
#     [1,4,7,11,15],
#     [2,5,8,12,19],
#     [3,6,9,16,22],
#     [10,13,14,17,24],
#     [18,21,23,26,30]
# ]
# target = 21
# print(searchMatrix(matrix, target))

def searchMatrix(matrix, target):
    maxCol = len(matrix[0]) - 1
    maxRow = len(matrix) - 1

    row = len(matrix) - 1
    col = 0
    
    while 0 <= col <= maxCol and 0 <= row <= maxRow:
        print(row)
        print(col)
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            row -= 1
        else:
            col += 1
    
    return False
    
matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
target = 13
print(searchMatrix(matrix, target))