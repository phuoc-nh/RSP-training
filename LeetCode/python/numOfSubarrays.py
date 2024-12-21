def numOfSubarrays(arr, k: int, threshold: int) -> int:
    res = 0
    curSum = sum(arr[0:k])
    if curSum / k >= threshold:
        res += 1
    
    for i in range(1, len(arr) - k + 1):
        print(arr[i+k-1], i)
        
        curSum -= arr[i-1]
        curSum += arr[i+k-1]
        
        if curSum / k >= threshold:
            res += 1
    
    print(res)
    return res
    
arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5


numOfSubarrays(arr, k, threshold)