from collections import Counter
def wordSubsets(words1, words2):
    count2 = {}
    
    for w in words2:
        countW = Counter(w)
        
        for c in countW:
            if c in count2:
                count2[c] = max(count2[c], countW[c])
            else:
                count2[c] = countW[c]
            
    res = []
    
    print(count2)
    for w in words1:
        count = Counter(w)
        found = True
        for k in count2.keys():
            if count2[k] > count[k]:
                found = False
                
        if found:
            res.append(w)    
            
    print(res)
    
    return res
    
    
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["lo","eo"]

wordSubsets(words1, words2)