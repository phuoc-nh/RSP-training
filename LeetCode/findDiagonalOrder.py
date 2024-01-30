from collections import defaultdict 
def findDiagonalOrder(nums):
    ROWS = len(nums)
    d = defaultdict(list)
    for i in range(ROWS-1, -1, -1):
        for j in range(len(nums[i])):
            diagonal = i + j
            d[diagonal].append(nums[i][j])
            
    res = []
    cur = 0
    while cur in d:
        res.extend(d[cur])        
        cur += 1
    print(res)
    return res
    

nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]

findDiagonalOrder(nums)