def isAlienSorted(words, order: str) -> bool:
    orderMap = {}
    
    for  i in range(len(order)):
        orderMap[order[i]] = i
        
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i+1]
        
        # check if w1 and w2 in order based on order map
        
        for j in range(len(w1)):
            if j >= len(w2):
                # ["apple","app"]
                # l > none character should none character should come first
                # if w1 has longer length than w2 and w1 come before w2 should return False
                return False
            
            if orderMap[w1[j]] > orderMap[w2[j]]:
                return False
            elif orderMap[w1[j]] == orderMap[w2[j]]:
                continue
            else: # the word in correct order no need to check the rest
                break
                
                
            
    return True
    
    
    
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"

res = isAlienSorted(words, order)
print('res', res)
