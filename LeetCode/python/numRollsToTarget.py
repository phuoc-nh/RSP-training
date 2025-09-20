def numRollsToTarget(n, k, target):
    res = 0
    cache = {}
    
    def dfs(i, cur):
        nonlocal res
        if i == n and cur == target:
            return 1

        if (i, cur) in cache:
            return cache[(i, cur)]
        
        total = 0
        for j in range(1, k + 1):
            if cur + j <= target:
                total += dfs(i + 1, cur + j)
        cache[(i, cur)] = total
        return total

    result = dfs(0, 0)
    print(result)
    return result


n = 1
k = 6
target = 3

numRollsToTarget(n,k,target)