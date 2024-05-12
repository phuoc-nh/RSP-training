import math

def isPrime(number):
    count = 1
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            count += 1
    return count == 1

def getValidKeyCount(keys):
    res = []
    for i in range(len(keys)):
        count = 0
        for j in range(2, math.floor(math.sqrt(keys[i])) + 1):
            if isPrime(j) and j * j <= keys[i]:
                count += 1
        res.append(count)
    print(res)
    return res
    
# print(isPrime(7))
for i in range(2, 100):
    print(i, isPrime(i))
getValidKeyCount(keys=[122, 465, 340, 291, 376, 105])