def canBeValid(s: str, locked: str) -> bool:
    lenS = len(s)
    if lenS % 2 == 1:
        return False
    
    listS = list(s)
    
    for i in range(len(locked)):
        if locked[i] == '0':
            listS[i] = '*'
    
    print(listS)
    
    stars = []
    openBracket = []
    
    for i in range(lenS):
        if listS[i] == '*':
            stars.append(i)
        elif listS[i] == '(':
            stars.append(i)
        else:
            if len(stars) == 0 and len(openBracket) == 0:
                return False
            
            if len(openBracket):
                openBracket.pop()
                continue
            # if not open bracket, use star to close
            stars.pop()
            
    
    print('stars', stars)
    print('openBracket', openBracket)
    
    if len(openBracket) > len(stars):
        return False
    
    while len(openBracket):
        top = openBracket[-1]
        if  top > stars.pop():
            return False
        
        openBracket.pop()
        
    return True
    
    
    
            
            
s = ")"
locked = "0"

# s = "))()))"
# locked = "010100"

res = canBeValid(s, locked)

print(res)