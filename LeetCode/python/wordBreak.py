def wordBreak(s, wordDit):
    dp = [False for i in range(len(s)+1)]
    dp[0] = True
    
    for i in range(1, len(s)+1):
        for word in wordDit:
            print('segment', s[i - len(word)+1:i+1])
            print('i', i)
            print('word', word)
            if i - len(word) < 0:
                continue
            if dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True
                # break
        print('==========')
    print(dp[len(s)])
    print(dp)    
    return dp[len(s)]

s = "applepenapple"
wordDict = ["apple","pen"]
wordBreak(s, wordDict)
