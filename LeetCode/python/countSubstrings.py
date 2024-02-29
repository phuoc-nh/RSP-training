def countSubstrings(s):
    res = 0
    for i in range(len(s)):
        left = i
        right = i
        
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            else:
                break
        
        left = i
        right = i+1
        
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            else:
                break
    print(res)
    return res
s = 'aaa'
countSubstrings(s)