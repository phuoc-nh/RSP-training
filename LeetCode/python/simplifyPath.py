def simplifyPath(path: str) -> str:
    stack = [''] # denotes first slash
    
    splitted = path.split("/")
    
    for i in range(1, len(splitted)):
        s = splitted[i]
        if s == '..':
            if len(stack) == 1:
                continue
            stack.pop()
        elif s == '.':
            pass
        elif s != '':
            print(">>>")
            stack.append(s)
            
            
    if len(stack) == 1:
        return '/'
    print(stack)
    
    return "/".join(stack)
            
    
path = "/.."
# path = "/home/user/Documents/../Pictures"
# path = "/.../a/../b/c/../d/./"
res = simplifyPath(path)
print(res)
