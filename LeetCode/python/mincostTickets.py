def mincostTickets(days, costs) -> int:
    costDays = [1, 7, 30]
    memo = {}
    def dfs(i):
        if i >= len(days):
            return 0
        
        if i in memo:
            return memo[i]
        
        res = 1e9
        prev = days[i]
        for j in range(3):
            nextDay = costDays[j] + prev
            k = i 
            while k < len(days) and nextDay > days[k]:
                k += 1
                
            res = min(res, costs[j] + dfs(k))
        memo[i] = res
        return res
    
    res = dfs(0)
    print(res)
    
    return res
    
days = [1,4,6,7,8,20]
costs = [2,7,15] # 1, 7, 30

mincostTickets(days, costs)