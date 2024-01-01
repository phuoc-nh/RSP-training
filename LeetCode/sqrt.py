def sqrt(x):
    res = 0
    l = 0
    r = x
    
    while l <= r:
        mid = (l + r) // 2
        print('mid', mid)
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
            
    return res
            
            
print(sqrt(8))