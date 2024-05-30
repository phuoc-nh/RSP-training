def equalSubstring(s, t, maxCost):
    temp = [] 
    for i in range(len(s)):
        temp.append(abs(ord(s[i]) - ord(t[i])))
    
    print(temp)
    
    l = 0
    r = 0
    curCost = 0
    res = 0
    
    while r < len(s):
        curCost += temp[r]
        # print(l, r, curCost)
        
        while curCost > maxCost:
            curCost -= temp[l]
            l += 1
        
        res = max(res, r-l+1)
        
        r += 1
         
    print(res)    
    return res
# s = "abcd"
# t = "bcdf"
# maxCost = 3

s = "abcd"
t = "cdef"
maxCost = 3

# s = "abcd"
# t = "acde"
# maxCost = 0

equalSubstring(s, t, maxCost)