def numTilings(n):
    MOD = 1e6 + 7
    if n <= 2:
        return n
    f = [0 for i in range(n+1)]
    p = [0 for i in range(n+1)]

    f[1] = 1
    f[2] = 2
    p[2] = 1
    
    for i in range(3, n):
        f[i] = (f[i-2] + f[i-2] + 2*p[i-1]) % MOD
        p[i] = (f[i-2] + p[i-1]) % MOD
    return f[n]

 