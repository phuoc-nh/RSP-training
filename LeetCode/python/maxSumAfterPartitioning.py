def maxSumAfterPartitioning(arr, k):
    dp = [n for n in arr]
    
    for i in range(len(arr)):
        curMaxEl = arr[i]
        dp[i] = arr[i] + (dp[i-1] if i-1 >= 0 else 0)
        for j in range(i-1, i-k, -1):
            if j < 0:
                break
            print('j', j)
            print('curMaxEl', curMaxEl)
            curMaxEl = max(curMaxEl, arr[j])
            print('i', i)
            print('j', j)
            dp[i] = max(dp[i], (i -j + 1) * curMaxEl + (dp[j-1] if j-1 >= 0 else 0))
        print('--------------')
            
    print(dp)
    return dp[len(arr) -1]

arr = [1,4,1,5,7,3,6,1,9,9,3]
k = 4
maxSumAfterPartitioning(arr, k)