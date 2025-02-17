def constructDistancedSequence(n: int):
    res = [0] * (n * 2 - 1)
    
    used = set()
    
    def backtrack(i):
        
        # base case
        if i == len(res): # all slots are filled
            return True
        
        for j in reversed(range(1, n+1)):
            # validate 
            if j in used:
                continue
                
            # check j != 1 and if positions are good
            if j > 1 and (i + j >= len(res) or res[i+j] != 0):
                continue
            
            used.add(j)
            res[i] = j
            if j > 1:
                res[i+j] = j 
                
            # define next index to backtrack
            next = i 
            
            while next < len(res) and res[next] != 0:
                next += 1
                
            if backtrack(next):
                return True
            
            
            # backtrack, remove last case
            
            used.remove(j)
            res[i] = 0
            if j > 1:
                res[i+j] = 0
        return False
    
        
    backtrack(0)
    
    # print(res)
    
    return res
    
    
    
n = 5
# [3,1,2,3,2]
constructDistancedSequence(n)