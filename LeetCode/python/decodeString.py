def decodeString(s: str) -> str:
    stack = []
    for x in s:
        if x == ']':
            chunk = []
            while len(stack) and stack[-1] != '[':
                chunk.append(stack.pop())
           
            chunk.reverse()
            chunk = "".join(chunk)
            stack.pop()
            
            
            number = []
            while len(stack) and stack[-1].isdigit():
                number.append(stack.pop())
            number.reverse()
            number = int("".join(number))
            
            
            
            stack.append(chunk * number)
            
            
        else:
            stack.append(x)
            
    print("".join(stack))
            
    return "".join(stack)
    
    
s = "100[leetcode]"

decodeString(s)