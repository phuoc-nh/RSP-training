def normalFibo(n):
    # fn = fn-1 + fn-2
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return normalFibo(n-1) + normalFibo(n-2)

def fiboCache(n): # Bottom up 
    f = [0 for i in range(n)]
    f[1] = 1

    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
    print(f)

print(fiboCache(6))