def doesValidArrayExist(derived) -> bool:
    res = [1] * len(derived)
    print(res)
    
    for i in range(1, len(derived)):
        res[i] = res[i-1] ^ derived[i-1]
        
    print(res)
    
    
    if res[-1] ^ res[0] == derived[-1]:
        return True
    
    return False
    
derived = [1,0]
res = doesValidArrayExist(derived)



print(res)