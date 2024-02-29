def areAlmostEqual(s1,s2):
    i = 0
    j = 0
    count = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            count += 1            
        i += 1
        j += 1
    return True if count in [0,2] and sorted(s1) == sorted(s2) else  False

s1 = 'bank'
s2 = 'kanb'
print(areAlmostEqual(s1,s2))