def minFlips(a,b,c):
    count = 0
    while a != 0 or b != 0 or c != 0:
        print(a,b,c)
        if c % 2 == 1:
            if a % 2 == 0 and b % 2 == 0:
                count += 1
        else:
            if a % 2 == 1:
                count += 1
            if b % 2 == 1:
                count += 1
                
        a = a >> 1
        b = b >> 1
        c = c >> 1
    return count

a = 4
b = 2
c = 7
print(minFlips(a,b,c))    