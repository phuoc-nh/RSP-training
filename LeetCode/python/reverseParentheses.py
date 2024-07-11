def reverseParentheses(s):
	# init stack
    stack = []
    # loop through s
    for i in range(len(s)):
        if s[i] == ')':
            temp = []
            while stack[-1] != '(':
                temp.append(stack.pop())
            
            stack.pop()
            
            for t in temp:
                stack.append(t)
        else:
            stack.append(s[i])
            
    
    print(''.join(stack))
    return ''.join(stack)
    # if )
    # temp 
    # while s[-1] is not (
    #   put in temp
    # this point s[-1] is (
    # pop out s[-1]
    # for x in temp
    #   put in s
    # else
    # put in stack
    
    
s = "(ed(et(oc))el)"

reverseParentheses(s)