t = int(input())

for i in range(t):
    lenS = int(input())
    string = input()
    res = 1
    for i in range(1, lenS-1):
        # print('>', string[i])
        if string[i-1] == string[i+1]:
            continue
        else:
            res += 1
    
    print(res)
    
    

    