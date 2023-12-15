def lengthOfLongestSubstringKDistinct(s, k):
    if k == 0:
        return 0
    
    i = 0
    j = 0
    m = {}
    res = 0
    
    while j < len(s) and i < len(s):
        m[s[j]] = m.get(s[j], 0) + 1
        # ? how to calculate current length
        # print('i j', i, j)
        # print('map', m)        
        if len(m) > k:
            # decrease s[i] in map if == 0 -> delete
            m[s[i]] -= 1
            if m[s[i]] == 0:
                del m[s[i]]
                
            m[s[j]] -= 1
            if m[s[j]] == 0:
                del m[s[j]]
            i += 1
        else:
            res = max(res, j - i + 1)
            j += 1
        # print('res', res)
        # print('==============')
    return res

s = "aa"
k = 1
print(lengthOfLongestSubstringKDistinct(s, k))
         
    