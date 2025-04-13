def countSymmetricIntegers(low: int, high: int) -> int:
    def isSym(i):
        i = list(str(i))
        
        if len(i) % 2 == 1:
            return False
        
        
        l = 0
        r = len(i) - 1
        left = 0
        right = 0
        while l < r:
            left += int(i[l])
            right += int(i[r])
            l += 1
            r -= 1
            
        return left == right
    
    res = 0
    for i in range(low, high+1):
        if isSym(i):
            res += 1
    
    print(res)
    return res
        
        
low = 1
high = 100

countSymmetricIntegers(low, high)