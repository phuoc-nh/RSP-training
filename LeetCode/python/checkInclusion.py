def checkInclusion(s1: str, s2: str) -> bool:
    counter1 = {}
    for c in s1:
        counter1[c] = 1 + counter1.get(c, 0)
    
    counter2 = {}
    
    l = 0
    
    for r in range(len(s2)):
        if s2[r] not in counter1:
            l = r + 1
            counter2 = {}
        else:
            counter2[s2[r]] = 1 + counter2.get(s2[r], 0)
            
            if counter2[s2[r]] > counter1[s2[r]]:
                # move left pointer
                while counter2[s2[r]] > counter1[s2[r]]:
                    counter2[s2[l]] -= 1
                    l += 1
            else:
                if counter1 == counter2:
                    return True
                
    
    
    return False
                    
    
    
s1 = "ooab"
s2 = "eidboaoo"

res=  checkInclusion(s1, s2)
print(res)