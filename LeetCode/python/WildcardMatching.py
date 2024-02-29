
def isMatch(s, p):
    lens = len(s)
    lenp = len(p)

    dp = [[False] * (lenp + 1) for i in range(lens+1)]
    dp[0][0] = True
    
    for i in range(1, lenp+1):
        if p[i-1] == '*':
            dp[0][i] = True
        else:
            break
    
    for i in range(1, lens + 1):
        for j in range(1, lenp + 1):
            # print(s[i-1], p[j-1])
            if s[i-1] == p[j-1] or p[j-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif s[i-1] != p[j-1]:
                dp[i][j] = False
    # for d in dp:
    #     print(d)

    return  dp[lens][lenp]
s = 'cb'
p = '?a'

print(isMatch(s,p))