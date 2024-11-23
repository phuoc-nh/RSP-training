def isAnagram(s, t):
    countS = {}
    countT = {}
    
    for c in s:
        countS[c] = countS.get(c, 0) + 1
    
    for c in t:
        countT[c] = countT.get(c, 0) + 1
        
    return countS == countT # to compare 2 reference
    
    
        
	
    
s = "racecar"   
t = "carrace"

print(isAnagram(s, t))