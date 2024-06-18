def judgeSquareSum(c):
    if c <= 2:
        return c 
    for i in range(c):
        l = 0
        r = c
        
        while l <= r:
            mid = (l+r) // 2
            total = i ** 2 + mid ** 2
            if total == c:
                return True
            elif total < c:
                l = mid + 1
            else:
                r = mid - 1
    return False

c = 3
print(judgeSquareSum(c))