def wordBreak(s, wordDict):
    res = []
    part = []
    def backtrack(j):
        
        if j == len(s):
            res.append(' '.join(part))
            return
        
        for i in range(j, len(s)):
            # print(s[j:i+1])
            if s[j:i+1] in wordDict:
                part.append(s[j:i+1])
                backtrack(i+1)
                part.pop()
        
    backtrack(0)

    
    print(res)
    return res
s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
# ["cats and dog","cat sand dog"]
wordBreak(s, wordDict)