def maxUncrossedLines(nums1, nums2) -> int:
    n = len(nums1)
    m = len(nums2)
    
    dp = [[0] * (n + 1) for i in range(m + 1)]
    
    for i in range(1, m+1):
        for j in range(1, n + 1):
            if nums1[j - 1] == nums2[i - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    for d in dp:
        print(d)
                
    return dp[m][n]
    
    
nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]

res = maxUncrossedLines(nums1, nums2)
print(res)