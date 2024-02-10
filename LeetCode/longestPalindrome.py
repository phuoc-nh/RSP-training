def longestPalindrome(s):
    left = 0
    right = 0
    maxLen = 0
    
    for i in range(len(s)):
        l = i
        r = i + 1
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    left = l
                    right = r
                l -= 1
                r += 1
            else:
                break
        
        l = i
        r = i
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    left = l
                    right = r
                l -= 1
                r += 1
            else:
                break
                
    # print(right, left)
    # print(s[left:right+1])
    return s[left:right+1]

s = "cbbd"
longestPalindrome(s)