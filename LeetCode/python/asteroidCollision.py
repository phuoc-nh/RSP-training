def asteroidCollision(asteroids):
    stack = []
    
    for i in range(len(asteroids)):
        
        if len(stack) == 0:
            stack.append(asteroids[i])
            continue
        
        if stack[-1] * asteroids[i] > 0:
            stack.append(asteroids[i])
            continue

        while len(stack) > 0 and stack[-1] * asteroids[i] < 0:
            if abs(asteroids[i]) == abs(stack[-1]):
                stack.pop()
                break
            elif abs(asteroids[i]) > abs(stack[-1]):
                stack.pop()
                # stack.append(asteroids[i])
            else:
                break
                
                
    
    
    print(stack)
    return stack
                    
    
    
    
asteroids = [5,10,-5]
asteroidCollision(asteroids)