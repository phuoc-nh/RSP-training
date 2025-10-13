def isMatch(s: str, p: str):
    
    def dfs(i, j):
        if i >= len(s) and j >= len(p):
            return True
        
        if j >= len(p):
            return False
        
        match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        
        if j < len(p) - 1 and p[j+1] == '*':
            # skip
            return dfs(i, j + 2) or (match and dfs(i+1, j))
            # not skip but has to match
        
        if match:
            return dfs(i+1, j+ 1)
        
        return False

    return dfs(0, 0)


s = "ab"
p = ".*c"

s = "aa"
p = "a"
res = isMatch(s, p)

print(res)