def smallestNumber(pattern: str) -> str:
    res = []
    stack = []
    
    
    
    for i in range(len(pattern) + 1):
        stack.append(str(i+1))
        
        while stack and (i == len(pattern) or pattern[i] == "I"):
            res.append(stack.pop())	
            
            
    print('res .>>', res)
    return ''.join(res)

# result = []
# num_stack = []

# # Iterate through the pattern
# for index in range(len(pattern) + 1):
# 	# Push the next number onto the stack
# 	num_stack.append(index + 1)

# 	# If 'I' is encountered or we reach the end, pop all stack elements
# 	if index == len(pattern) or pattern[index] == "I":
# 		while num_stack:
# 			result.append(str(num_stack.pop()))

# return "".join(result)



pattern = "IIIDIDDD"
		   
res = smallestNumber(pattern)