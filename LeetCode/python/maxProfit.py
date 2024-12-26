def maxProfit(prices) -> int:
    
    res = 0
    
    l = 0
    
    for r in range(len(prices)):
        diff = prices[r] - prices[l]
        
        if diff < 0:
            l = r
        else:
            res = max(res, diff)
    
    print(res)
    return res
    
prices = [7,6,4,3,1]

maxProfit(prices)