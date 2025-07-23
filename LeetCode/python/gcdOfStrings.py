def isGcd(long, part):
    if len(long) % len(part) != 0:
        return False
    print('part', part)
    for i in range(0, len(long), len(part)):
        print('i', i)
        print(long[i:i+len(part)])
    print('====')
 
 
isGcd("ABCABC", "AB")