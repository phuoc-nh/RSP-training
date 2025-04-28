def validPalindrome( s: str) -> bool:
    
    def isPalindrome(l, r):
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            return False
        
        return True
    
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
            
        else:
            return isPalindrome(l+1, r) or isPalindrome(l, r-1)
    
    return True

s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
res = validPalindrome(s)

print(res)

