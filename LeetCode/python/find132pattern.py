def find132pattern(nums) -> bool:
    stack = [] # val, cur min
    
    stack.append((nums[0], nums[0]))
    
    for i in range(1, len(nums)):
        print(nums[i], stack)
        
        
        newMin = min(stack[-1][1], nums[i])
        
        
        while len(stack) and nums[i] > stack[-1][0]:
            stack.pop()
            
        if len(stack) and nums[i] < stack[-1][0] and nums[i] > stack[-1][1]:
            return True
        stack.append((nums[i], newMin))
        
    print(stack)
        
    return False
        
    
    
    
nums = [-1,3,2,0]


res = find132pattern(nums)

print(res)