def buildMatrix(k: int, rowConditions, colConditions):
    # build row adj list
    adjRow = [[] for i in range(k+1)]
    for u, v in rowConditions:
        adjRow[u].append(v)
        
    adjCol = [[] for i in range(k+1)]
    for u, v in colConditions:
        adjCol[u].append(v)

    
    def dfs(src, visited, path, adj, res):
        if src in path:
            return False
        
        if src in visited:
            return True
        
        visited.add(src)
        path.add(src)
        for v in adj[src]:
            if not dfs(v, visited, path, adj, res):
                return False
        
        # backtrack visited
        path.remove(src)
        res.append(src)
        
        return True
    
    visited = set()
    path = set()
    rowSort = []
    for i in range(1, k+1):
        if not dfs(i, visited, path, adjRow, rowSort):
            return []
    
    visited = set()
    path = set()
    colSort = []
    for i in range(1, k+1):
        if not dfs(i, visited, path, adjCol, colSort):
            return []
    
    rowSort =  list(reversed(rowSort))
    rowValueToIndex = {rowSort[i]: i  for i in range(len(rowSort))}
        
    colSort =  list(reversed(colSort))
    colValueToIndex = {colSort[i]: i  for i in range(len(colSort))}
    
    matrix = [[0] * k for i in range(k)]
    for i in range(1, k + 1):
        row = rowValueToIndex[i]
        col = colValueToIndex[i]    
        matrix[row][col] = i
    
    return matrix

k = 3
rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]
res = buildMatrix(k, rowConditions, colConditions)
for x in res:
    print(x)