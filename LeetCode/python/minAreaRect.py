def minAreaRect(points):
    setList = set()
    for p in points:
        setList.add((p[0], p[1]))
        
    points.sort()
    print(points)
    res = float('inf')
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            if (x1, y2) in setList and (x2, y1) in setList and x2 != x1 and y2 != y1:
                res = min(res, abs((x2 - x1) * (y2 - y1)))
    
    print(res)
    return res

points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
minAreaRect(points)        
            
            