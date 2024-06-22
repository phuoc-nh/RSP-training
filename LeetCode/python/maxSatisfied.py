def maxSatisfied(customers, grumpy, minutes):
    total = 0
    for i in range(len(customers)):
        if grumpy[i] == 0:
            total += customers[i]
    
    if minutes >= len(customers):
        for i in range(len(customers)):
            if grumpy[i] == 1:
                total += customers[i]
        
        return total

    for i in range(0, minutes, 1):
        if grumpy[i] == 1:
            total += customers[i]
        
    res = total
    i = 1
    j = i + minutes - 1
    cur = total
    while j < len(customers):
        if grumpy[i-1] == 1:
            cur -= customers[i-1]
        
        if grumpy[j] == 1:
            cur += customers[j]
        res = max(res, cur)
        
        i += 1
        j += 1
    
    print(res)
    return res
        
        
customers = [1]
grumpy = [0]
minutes = 1

res = maxSatisfied(customers, grumpy, minutes)
print(res)