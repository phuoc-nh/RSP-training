def appendCharacters(s, t):
    i = 0
    j = 0
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1
    print(j)
    if j == len(t):
        return 0
    
    return len(t) - j

s = "z"
t = "abcde"

print(appendCharacters(s, t))