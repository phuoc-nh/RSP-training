def plusOne(digits):
    flag = 1
    for i in range(len(digits) - 1, -1, -1):
        sum = flag + digits[i]
        if sum >= 10:
            digits[i] = 0
            flag = 1
        else:
            flag = 0
            digits[i] = sum

    if flag > 0:
        # append 0 at head of array
        digits.insert(0, 1)
    
    return digits

digits = [9,9,9]
print(plusOne(digits))

# Time spent: 15m