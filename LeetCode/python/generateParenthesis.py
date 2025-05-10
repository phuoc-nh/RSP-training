def generateParenthesis(n: int):
    
    res = []
    def dfs(open, close, cur):
        if open == 0 and close == 0:
            res.append(cur)
            return
        
        if open == 0:
            dfs(open, close - 1, cur + ")")
        else:
            if open == close:
                dfs(open - 1, close, cur + "(")
            else:
                dfs(open - 1, close, cur + "(")
                dfs(open, close - 1, cur + ")")

    
    dfs(n, n, "")
    print(res)
    
    return res

                
        
        
generateParenthesis(1)