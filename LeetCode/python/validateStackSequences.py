def validateStackSequences(pushed, popped) -> bool:
    # pushed.reverse()
    popped.reverse()
    stack = []
    
    for p in pushed:
        stack.append(p)
        
        while len(stack) and len(popped) and stack[-1] == popped[-1]:
            stack.pop()
            popped.pop()  
    
    return len(stack) == 0
    
    
pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]

res = validateStackSequences(pushed, popped)
print(res)