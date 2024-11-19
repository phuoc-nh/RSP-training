def decrypt(code, k):
    res = code.copy()
    
    for i in range(len(code)): 
        if k == 0:
            res[i] = 0
            
        if k > 0:
            temp = 0
            for j in range(k):
                id = (i + j + 1) % len(code)
                print(id)
                temp += code[id]
                res[i] = temp
                
        if k < 0:
            temp = 0
            for j in range(k * -1):
                id = (i - j - 1) if (i - j - 1) >= 0 else len(code) + (i - j - 1)
                temp += code[id]
                res[i] = temp
    print(res)     
    return res
code = [2,4,9,3]
k = -2

# -1 -> 3
# -2 -> 2
# -3 -> 1
# -4 -> 0

decrypt(code, k)