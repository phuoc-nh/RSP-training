import heapq
def maximumSum(nums) -> int:
    
    numbMap = {} # number -> heap q
    
    
    for n in nums:
        origin = n
        sumN = 0
        while n > 0:
            remain = n % 10
            # print(remain)
            n = n // 10
            # print(n)
            sumN += remain
            
        if sumN in numbMap:
            heapq.heappush(numbMap[sumN], -origin)
        else:
            numbMap[sumN] = [-origin]
    
    
    res = -1 
    for k in numbMap:
        if len(numbMap[k]) <= 1:
            continue
        
        numb1 = -heapq.heappop(numbMap[k])     
        numb2 = -heapq.heappop(numbMap[k])     
        
        res = max(res, numb1 + numb2)
        
    print(res)
        
    # print(numbMap)
    
    return res
nums = [18,43,36,13,7]
maximumSum(nums)