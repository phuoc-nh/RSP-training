import math
def isPerfectSquare(num: int) -> bool:
    l = 1
    r = num
    
    while l <= r:
        m = (l + r) // 2
        mm = m * m
        if mm == num:
            return True
        elif mm > num:
            r = m -1
        else:
            l = m + 1
            
    
    return False

num = 14
res = isPerfectSquare(num)
print(res)