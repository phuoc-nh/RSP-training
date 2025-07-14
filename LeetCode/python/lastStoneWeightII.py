def lastStoneWeightII(stones):
    # split stones into 2 piles
    # find the minimum differences between them
    total = sum(stones)
    half = total // 2
    cache = {}
    
    def dfs(i, cur): # current index in stones list, cur total
        if cur >= half or i >= len(stones):
            # find the first half which is cur
            # calculate second hafl
            second = total - cur
            return abs(cur - second)
        if (i, cur) in cache:
            return cache[(i, cur)]
        
        cache[(i, cur)] = min(dfs(i+1, cur + stones[i]), dfs(i+1, cur))
        
        return cache[(i, cur)]
    
    res = dfs(0, 0)
    
    print(res)
    return res
    
stones = [2,7,4,1,8,1]
lastStoneWeightII(stones)