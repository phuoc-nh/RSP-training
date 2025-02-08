def queryResults(limit: int, queries):
    ballColoMap = {}
    colors = {}
    res = []
    
    for ball, color in queries:
        
        if ball in ballColoMap:
            colors[ballColoMap[ball]] -= 1
            if colors[ballColoMap[ball]] == 0:
                del colors[ballColoMap[ball]]
                
        ballColoMap[ball] = color
        
        if color in colors:
            colors[color] += 1
        else:
            colors[color] = 1
        
        
        res.append(len(colors.keys()))
    
    print(res)
    
    return res
limit = 4
queries = [[0,1],[1,4],[1,1],[1,4],[1,1]]



queryResults(limit, queries)