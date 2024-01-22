import math

def sumSubarrayMins(arr):
    res = 0
    stack = []
    
    for i, n in enumerate(arr):
        while stack and n < stack[-1][1]:
            j, m = stack.pop()
            right = i - j
            left = j - stack[-1][0] if stack else j+1
            res += m * right * left   
            
        stack.append((i, n)) 
        

    for i in range(len(stack)):
        j, m = stack[i]
        
        left = j - stack[i-1][0] if i > 0 else j + 1
        right = len(arr) - j 
        res += m * right * left
    
    print(res)
    return res % 1_000_000_007

arr = [3,1,2,4]
sumSubarrayMins(arr)

# for i, n in enumerate(arr):
#         while stack and n < stack[-1][1]:
#             j, m = stack.pop()
#             left = j - stack[-1][0] if stack else j + 1
#             print('left', left)
#             right = i - j
#             print('right', right)
#             res = (res + m * left * right)
#         stack.append((i, n))

#     for i in range(len(stack)):
#         j, n = stack[i]

#         left = j - stack[i - 1][0] if i > 0 else j + 1
#         right = len(arr) - j 
        
#         res += n * left * right