def bruteForce(s1, s2):
    finalRes = 0
    
    for i in range(len(s1)):
        k = i
        j = 0
        res = 0
        while k < len(s1) and j < len(s2):
            if s1[k] == s2[j]:
                res += 1
                k += 1
                j += 1
            else:
                j += 1
        # print()
        finalRes = max(res, finalRes)    
    print(finalRes)
s1 = ['e', 'd', 'x']
s2 = ['a', 'e', 'c', 'd', 'g']
bruteForce(s1, s2)