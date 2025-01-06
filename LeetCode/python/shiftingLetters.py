def shiftingLetters(s: str, shifts) -> str:
    alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
    
    print(alphabets)
    
    map = {}
    for i in range(len(alphabets)):
        map[alphabets[i]] = i

    listS = list(s)
    for start, end, dir in shifts:
        for i in range(start, end + 1):
            c = listS[i]
            # print(c)
            if dir == 0:
                listS[i] = alphabets[map[c] - 1] 
            else:
                # print('map[c] + 1', map[c] + 1)
                listS[i] = alphabets[map[c] + 1 if map[c] + 1 <= 25 else 0]
                
    # print(listS) 
    
    return "".join(listS)
    
    
# s = "abc"
# shifts = [[0,1,0],[1,2,1],[0,2,1]]

s = "dztz"
shifts = [[0,0,0],[1,1,1]]

res = shiftingLetters(s, shifts)
print(res)