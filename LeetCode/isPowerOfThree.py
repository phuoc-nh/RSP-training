def isPowerOfThree(n):
    print(round(n ** 1/3))
    print(round(n ** 1/3) ** 3)
    return round(n ** 1/3) ** 3 == n

isPowerOfThree(27)