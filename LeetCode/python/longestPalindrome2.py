from collections import Counter
def longestPalindrome(words) -> int:
    counter = Counter(words)
    difference = 0
    identical = []
    visited = set()
    for k in counter:
        if k[0] == k[1]:
            identical.append(counter[k])
        else:
            # if k in visited:
            #     continue
            reverse = k[1] + k[0]
            if reverse in counter:
                difference += min(counter[k], counter[reverse]) * 2
    
    print(counter) 
    odds = [x for x in identical if x % 2 == 1]
    even = [x for x in identical if x % 2 == 0]
    resEven = 0
    
    for x in even:
        resEven += x * 2
        
    if len(odds):
        maxi = max(odds)
        maxId = odds.index(maxi)
        resIden = maxi * 2
        
        for i in range(len(odds)):
            if i == maxId:
                continue
            print('i', i)
            if odds[i] % 2 == 0:
                resIden += odds[i] * 2
            else:
                resIden += (odds[i] - 1) * 2
                
    
        return resEven + resIden + difference

            

    # print(counter) 
    # print(resIden)   
    # print(difference)  
    
    # print(resIden + difference)
    return difference + resEven
    # return identical + difference    


words = ["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"]
res = longestPalindrome(words)
print('res', res)

# Counter({'lb': 4, 'bb': 3, 'bx': 3, 'xx': 3, 'll': 2, 'lx': 2, 'xb': 1, 'bl': 1, 'xl': 1})
