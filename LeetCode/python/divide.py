def divide(dividend: int, divisor: int) -> int:
    isNeg = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
    
    dividend = abs(dividend)
    divisor = abs(divisor)
    res = 0
    while dividend >= divisor:
        counter = 1
        dec = divisor
        while dividend >= dec:
            res += counter
            counter *= 2
            dividend -= dec
            dec *= 2
            
    return -res if isNeg else res


res = divide(7, -3)
print(res)