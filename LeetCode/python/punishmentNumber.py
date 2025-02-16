def punishmentNumber(n: int) -> int:
    #                36           1296
    def partition(i, target, cur, square):
        
        if i == len(square) and target == cur:
            return True
        
        for j in range(i, len(square)):
            if partition(j + 1, target, cur + int(square[i:j+1]), square):
                return True
            
        return False
    
    
    res = 0
    
    for i in range(n+1):
        if partition(0, i, 0, str(i * i)):
            # print('i * i', i * i, i)
            res += i * i
            
    print(res)
    return res
    
        
    
        
n = 10
punishmentNumber(n)


