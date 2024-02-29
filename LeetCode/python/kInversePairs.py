def kInversePairs(n, k):
    MOD = 1_000_000_007
    cache = {}
    def count(n, k):
        if k < 0:
            return 0
        if n == 0:
            return 1 if k == 0 else 0
        
        if (n, k) in cache:
            return cache[(n, k)]
        
        cache[(n, k)] = 0
        for i in range(n):
            cache[(n, k)] += count(n-1, k - i)
            
        return cache[(n, k)]

    return count(n, k) % MOD

n = 3 
k = 1

print(kInversePairs(n, k))