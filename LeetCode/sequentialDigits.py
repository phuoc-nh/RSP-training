def sequentialDigits(low, high):
    res = []
    lowDigits = len(str(low))
    highDigits = len(str(high))

    sample = '123456789'

    for i in range(lowDigits, highDigits + 1):
        for j in range(len(sample) - i + 1):
            print(sample[j:j + i])
            num = int(sample[j:j + i])
            if low <= num <= high:
                res.append(num)

    return res
    

low = 1000
high = 13000

sequentialDigits(low, high)