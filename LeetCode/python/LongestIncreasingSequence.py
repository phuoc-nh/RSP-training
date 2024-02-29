# def bruteForce():

def lcs(arr):
    dp = [1 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = dp[j] + 1
    
    print(dp)
    
arr = [2,5,12,3,10,6,8]
lcs(arr)
    