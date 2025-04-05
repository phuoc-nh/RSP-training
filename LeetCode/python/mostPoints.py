def mostPoints( questions) -> int:
    cache = {}
    n = len(questions)
    def helper(i):
        if i >= n:
            return 0
        
        if i in cache:
            return cache[i]
        
        res = max(helper(i+1) , helper(i + 1 + questions[i][1]) + questions[i][0])
        cache[i] = res
        return res    
    
    print(helper(0))
    
    return helper(0)
    
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]

mostPoints(questions)