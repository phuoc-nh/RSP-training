def mySqrt(x: int) -> int:
    
    
    l = 0
    r = x
    
    while l <= r:
        m = (l + r) // 2
        
        if m * m == x:
            return m
        elif m * m > x:
            r = m - 1
        else:
            l = m + 1
            
    print(l, r)
    
    return r
    
res = mySqrt(25)
print('res', res)
    