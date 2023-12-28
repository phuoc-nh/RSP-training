from collections import Counter

def firstUniqChar(s):
    c = Counter(s)
    for i in range(len(s)):
        if c[s[i]] == 1:
            return i
        
    return -1

s = "aabb"
print(firstUniqChar(s))