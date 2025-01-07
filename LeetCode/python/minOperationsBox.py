def minOperations(boxes: str):
    res = [0] * len(boxes)
    prefix = [0] * len(boxes)
    # for i in range(len(boxes)):
    #     for j in range(len(boxes)):
    #         if i == j:
    #             continue
            
    #         if boxes[j] == '1':
    #             res[i] += abs(i - j)
    
    balls = 0
    for i in range(0, len(boxes)):
        if i > 0:
            prefix[i] += prefix[i-1] + balls 
        
        if boxes[i] == '1':
            balls += 1

    balls = 0
    suffix = [0] * len(boxes)
    for i in range(len(boxes)-1, -1, -1):
        if i < len(boxes) - 1:
            suffix[i] += suffix[i+1] + balls
        
        if boxes[i] == '1':
            balls += 1
            
    # print(prefix)
    # print(suffix)
        
    for i in range(len(boxes)):
        res[i] = suffix[i] + prefix[i]
        
    return res
    
boxes = "001011"

minOperations(boxes)