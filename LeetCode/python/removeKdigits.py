def removeKdigits(num: str, k: int) -> str:
    listNum = []
    
    for i in range(len(num)):
        # listNum.append(num[i])
        while len(listNum) and k > 0 and num[i] < listNum[-1]:
            listNum.pop()
            k -= 1
            
        listNum.append(num[i])
        
    print(listNum)
    
    while len(listNum) and listNum[0] == 0:
        listNum.pop(0)
    
    
    
    return "".join(listNum)
    
    
num = "10"
k = 2

res = removeKdigits(num, k)
print(res)
