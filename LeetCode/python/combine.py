def combine(n: int, k: int):
    res = []
    def backtrack(cur, i):
        # define base case
        # len cur == k -> append to res and return 
        print('cur', cur)
        if len(cur) == k:
            res.append(cur.copy())
        
        # 
        for j in range(i+1, n+1):
            cur.append(j)
            backtrack(cur, j)
            cur.pop()
	
    for i in range(1, n+1):
        
        backtrack([i], i)
    
    print(res)
    
    return res
        
n = 4
k = 2


combine(n, k)
    
# [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

# 1, 2, 3 ,4