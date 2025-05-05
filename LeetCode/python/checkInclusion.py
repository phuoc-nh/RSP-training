from collections import Counter
def checkInclusion(s1: str, s2: str) -> bool:
    counter1 = Counter(s1)
    counter2 = {}
    l = 0
    
    print(counter1)
    
    def valid(c1, c2):
        # print('Counter 2', c2)
        for k in c2:
            if k not in c1 or c2[k] > c1[k]:
                return False
        
        return True
        
    
    for r in range(len(s2)):
        counter2[s2[r]] = counter2.get(s2[r], 0) + 1
 
        # isValid = valid(counter1, counter2)
        # print('counter2', counter2, l, r, isValid)
        while not valid(counter1, counter2) and l < r:
            counter2[s2[l]] -= 1
            if counter2[s2[l]] == 0:
                del counter2[s2[l]]
            l += 1
        print('after counter2', counter2, l, r)
        if len(counter1) == len(counter2):
            foundAnswer = True
            for k in counter2:
                if k not in counter1:
                    foundAnswer = False
                    break
                if counter2[k] != counter1[k]:
                    foundAnswer = False
                    break
            
            if foundAnswer:
                return True
        print('=====')
    
    return False
                        
            
            

    
s1 = "adc"
s2 = "dcda"

res= checkInclusion(s1, s2)
print(res)