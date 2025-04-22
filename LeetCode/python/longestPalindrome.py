def longestPalindrome(s: str) -> str:
    curMax = 0
    res = ""
    
    i = 0
    
    while i < len(s):
        print('i', i)
        cur = 1
        left = i - 1
        
        # to find identical adjacent chars
        while i < len(s)  - 1 and s[i] == s[i+1]:
            i += 1
            cur += 1
            
        # to expand to left and right side
        right = i + 1
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                cur += 2
                left -= 1
                right += 1
            else:
                break
            
        if cur > curMax:
            curMax = cur
            res = s[left+1:right]
            
        i += 1
            
    
    print(res)
    return res
        
    
    
    
    
s = "cbbbbbbbbbbbbxcaaacx"

longestPalindrome(s)