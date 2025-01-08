def suggestedProducts(products, searchWord: str):
    
    products.sort()
    
    l = 0
    lenPro = len(products)
    res = []
    for i in range(len(searchWord)):
        temp = []
        
        while l < lenPro and (len(products[l]) <= i or products[l][i] != searchWord[i]):
        # while i < len(products[l]) and l < lenPro and searchWord[i] != products[l][i]:
            l += 1
            
            print(l)
            
        for j in range(l, min(l+3, lenPro)):
            print('ii', i)
            print('products[j]', products[j])
            if i < len(products[j]) and products[j][0:i+1] == searchWord[0:i+1]:
                
                temp.append(products[j])
                
        res.append(temp)
        
        
    print(products)
    print(res)
    print(searchWord[1:2])
    return res
    
products = ["mobile","mouse","moneypot","monitor","mousepad",'asdzxc', "werdf", "zxc", "ff"]
searchWord = "mousee"


# products = ["havana"]

# searchWord = "tatiana"
suggestedProducts(products, searchWord)