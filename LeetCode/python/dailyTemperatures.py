def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    
    monoStack = []
    
    for i in range(len(temperatures)):
        temp = temperatures[i]
        if len(monoStack) == 0:
            monoStack.append((i, temp))
            continue
        
        if temp <= monoStack[-1][1]:
            monoStack.append((i, temp))
            continue
        # days = 1
        while len(monoStack) > 0 and temp > monoStack[-1][1]:
            index, _ = monoStack.pop()
            res[index] = i - index
            
        monoStack.append((i, temp))
        
    # print(monoStack)
    # print(res)
                
    return res
    
temperatures = [30,60,90]
dailyTemperatures(temperatures)