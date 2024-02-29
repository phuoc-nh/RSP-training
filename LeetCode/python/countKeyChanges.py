def countKeyChanges(s):
    count = 0
    for i in range(1, len(s)):
        if s[i].lower() != s[i-1].lower():
            count += 1
            
    # print(count)
    return count

s="AaAaAaaA"
countKeyChanges(s)