def lenLongestFibSubseq(arr) -> int:
    arrSet = set(arr)
    
    print(arrSet)
    res = 0    
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            temp = 2
            cur = arr[i] + arr[j]
            prev = arr[j]
            
            while cur in arrSet:
                
                temp += 1
                tempPrev = prev
                prev = cur
                cur = cur + tempPrev
            res = max(res, temp)
            
    print(res)
    
    return res if res >= 3 else 0
    
    
arr = [1,3,7,11,12,14,18]

lenLongestFibSubseq(arr)