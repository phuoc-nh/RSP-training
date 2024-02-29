def getSum(a,b):
    maxN = 32
    bina = bin(a if a>=0 else ~(-a)+(1<<32)+1)[2:].zfill(32)
    binb = bin(b if b>=0 else ~(-b)+(1<<32)+1)[2:].zfill(32)

    flag = '0'
    res = [0] * maxN
    print(bina)
    print(binb)
    d = {   # [sum, flag]
        '000': ['0', '0'],
        '001': ['1', '0'],
        '010': ['1', '0'],
        '011': ['0', '1'],
        '100': ['1', '0'],
        '101': ['0', '1'],
        '110': ['0', '1'],
        '111': ['1', '1'],
    }

    for i in range(maxN - 1, -1, -1):
        concat = bina[i] + binb[i] + flag
        sum, flag = d[concat]
        res[i] = sum
    print(''.join(res)) 
    if res[0] == '1':
        for i in range(len(res)):
            res[i] = '1' if res[i] == '0' else '0'
        return -(int(''.join(res), 2) + 1)
    return int(''.join(res), 2)
a = 41
b = -3

print(getSum(a, b))