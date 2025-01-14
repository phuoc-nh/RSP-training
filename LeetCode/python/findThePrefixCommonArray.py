def findThePrefixCommonArray(A, B):
    
    setA = set()
    setB = set()
    
    res = []
    count = 0
    for i in range(len(A)):
        
        setA.add(A[i])
        setB.add(B[i])
        
        if A[i] == B[i]:
            count += 1
            res.append(count)
            continue
        
        
        if A[i] in setB:
            count += 1
            
        if B[i] in setA:
            count += 1
        
        res.append(count)
    
    print(res)
    return res
    
A = [2,3,1]
B = [3,1,2]

findThePrefixCommonArray(A, B)