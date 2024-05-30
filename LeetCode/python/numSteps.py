def numSteps(s):
    
    def plusOne(s):
            
        flag = True
        s = list(s)
        print(s)
        for i in range(len(s) -1, -1, -1):
            if s[i] == '0' and flag:
                s[i] = '1'
                flag = False
            elif s[i] == '1' and flag:
                s[i] = '0'
                flag = True
                
        if flag:
            return '1' + ''.join(s)
        
        return ''.join(s)
    res = 0
    # print(plusOne(s))
    while s != '1':
        if s[len(s)-1] == '0':
            s = s[:-1]
        else:
            s = plusOne(s)
        res += 1
    print(res)
    return res
s = "1"
numSteps(s)