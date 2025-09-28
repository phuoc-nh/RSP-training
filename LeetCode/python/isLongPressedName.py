def isLongPressedName(name: str, typed: str) -> bool:
    
    i = 0
    j = 0
    
    # if name [i] != name[j]
    # return False
    # else
    # move j to next different character
    
    while i < len(name) and j < len(typed):
        if name[i] != typed[j]:
            return False
        # count how many same char in name
        # count how many same char in typed
        # if count in typed >= count in name -> good
        # return false
        c1 = 1
        while i < len(name) - 1 and name[i] == name[i+1]:
            c1 += 1
            i += 1
        
        c2 = 1
        while j < len(typed) - 1 and typed[j] == typed[j+1]:
            c2 += 1
            j += 1
            
        if c2 < c1:
            return False

        i += 1
        j += 1
        
    print(i, j)
    if j < len(typed):
        return False
    return True
    
    
name = "alex"
typed = "aaleex"

# name = "leelee"
# typed = "lleeelee"

name = "alex"
typed = "aaleexa"
# true
res = isLongPressedName(name, typed)
print('res', res)