def wordBreak(s: str, wordDict) -> bool:
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        
        for w in wordDict:
            print('diff', i - len(w))
            if i - len(w) < 0:
                continue
            
            if dp[i - len(w)] == True and s[i-len(w):i] == w:
                dp[i] = True
            
    print(dp)
    return dp[-1]
    
        

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

s = "leetcode"
wordDict = ["leet","code"]

wordBreak(s, wordDict)
