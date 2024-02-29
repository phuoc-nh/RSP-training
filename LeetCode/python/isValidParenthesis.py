def isValid(s):
    stack = []
    
    for c in s:
        print(c)
        if c in ['(', '[', '{']:
            stack.append(c)
            continue
        
        if c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
        elif c == '}':
            print('c', c)
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(c)
                
    print('>>>', stack, len(stack))
    return len(stack) == 0

s = '(]'

print(isValid(s))