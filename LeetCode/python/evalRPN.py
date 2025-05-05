def evalRPN(tokens):
    
    s = []
    for t in tokens:
        # if digit
        print(s)
        if t in ['+', '-', '*', '/']:
            first = s.pop()
            sec = s.pop()
            
            if t == '+':
                s.append(first + sec)
            elif t == '*':
                s.append(first * sec)
            elif t == '/':
                s.append(int(sec / first) )
            else:
                s.append(sec - first )
        else:
            s.append(int(t))
            
                
    print(s)
    
    return s[-1]
    
    
    

tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
evalRPN(tokens)