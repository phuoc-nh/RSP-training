def numRollsToTarget(n, k, target):
	MOD = 1_000_000_000 + 7
	cache = {}

	def dfs(n, cur):
		if n == 0:
			return 1 if cur == 0 else 0
		if (n, cur) in cache:
			return cache[(n, cur)]
		cache[(n, cur)] = 0
		for i in range(1, k+1):
			cache[(n, cur)] += dfs(n-1, cur - i) % MOD

		return cache[(n, cur)]

	r = dfs(n, target)	
	print(r)
	return r


n = 30
k = 30
target = 500

numRollsToTarget(n,k,target)