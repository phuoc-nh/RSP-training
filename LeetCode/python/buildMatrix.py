def buildMatrix(k: int, rowConditions, colConditions):
    rowAdj = [[] for i in range(k+1)]
    colAdj = [[] for i in range(k+1)]
    
    for u, v in rowConditions:
        rowAdj[u].append(v)
        
    for u, v in colConditions:
        colAdj[u].append(v)
    
    print(rowAdj)
    def dfs(cur, visited, path, toposort, adj):
        if cur in path:
            return False
        if cur in visited:
            return True
        
        

        visited.add(cur)
        path.add(cur)
        
        for nei in adj[cur]:
            if not dfs(nei, visited, path, toposort, adj):
                return False
            
        path.remove(cur)
        toposort.append(cur)
        return True
    
    sortedRows = []
    visited = set()
    
    for i in range(1, k+1):
        path = set()
        if not dfs(i, visited, path, sortedRows, rowAdj):
            return []
        
    sortedRows.reverse()
    print(sortedRows)
    
    sortedCols = []
    visited = set()
    
    for i in range(1, k+1):
        path = set()
        if not dfs(i, visited, path, sortedCols, colAdj):
            return []
        
    sortedCols.reverse()
    print(sortedCols)
    
    res = [[0] * k for i in range(k) ]
    valToIdRow = {}
    for i in range(len(sortedRows)):
        valToIdRow[sortedRows[i]] = i
        
    valToIdCol = {}
    for i in range(len(sortedCols)):
        valToIdCol[sortedCols[i]] = i
    
    for i in range(1, k+1):
        x = valToIdRow[i]
        y = valToIdCol[i]
        res[x][y] = i
    
    return res

k = 3
rowConditions = [[1,2],[2,3],[3,1],[2,3]]
colConditions = [[2,1]]
res = buildMatrix(k, rowConditions, colConditions)
for x in res:
    print(x)
# 1 -> 2 -> 3
# 2, 1, 3
# or 
# 2, 3, 1

# 1 --> 2
#     /
#    /
#   3

# 3 --> 2 --> 1
# 3