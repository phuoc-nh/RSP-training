def maximumOddBinaryNumber(s):
    listStr = list(s)
    left = 0
    for i in range(len(listStr)):
        if listStr[i] == '1':
            listStr[i], listStr[left] = listStr[left], listStr[i]
            left+=1
    print(''.join(listStr))
     
    listStr[left-1], listStr[len(listStr)-1] = listStr[len(listStr) -1], listStr[left-1]
    print(''.join(listStr))
    return ''.join(listStr)
    
    
maximumOddBinaryNumber("010")