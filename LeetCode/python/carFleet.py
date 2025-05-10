def carFleet(target: int, position, speed) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    print(pair)
    stack = []
    for p, s in pair:  # Reverse Sorted Order
        timeToTarget = (target - p) / s
        print('>>', timeToTarget)
        
        if len(stack) and timeToTarget <= stack[-1]:
            continue
        else:
            stack.append(timeToTarget)
            
        
    print(len(stack))
        
        # if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #     stack.pop()
    return len(stack)
    
    
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

# target = 100
# position = [0,2,4]
# speed = [4,2,1]

carFleet(target, position, speed)