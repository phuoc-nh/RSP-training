def multiply(num1: str, num2: str) -> str:
    if num1 == '0' or num2 == '0':
        return '0'
    
    def singleMul(num1, digit):
        carry = 0
        res = [None] * len(num1)
        for i in range(len(num1) - 1, -1, -1):
            n = int(num1[i])
            
            prod = n * digit + carry
            res[i] = prod % 10
            carry = prod // 10
        if carry:
            res.insert(0, carry)
        
        
        return int(''.join(map(str, res)))
    # singleMul('999', 9)
    res = 0
    for i in range(len(num2) - 1, -1, -1):
        power = len(num2) - i - 1
        
        res += singleMul(num1, int(num2[i])) * 10 ** power
    
    
    return str(res)
        
num1 = "123"
num2 = "456"
multiply(num1, num2)
            