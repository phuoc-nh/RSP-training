def largestIsland(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    
    visited = set()
    coordinates_island = {}
    island_area = {}
    island_count = 0
    
    def dfs(i, j):
        nonlocal island_count
        stack = []
        stack.append((i, j))
        
        area = 0
        temp_visited = set()
        # visited.add((i, j))
        # temp_visited.add((i, j))
        # print('i, j')
        
        while len(stack):
            r, c = stack.pop()
            print('.>>>>>', r, c, stack)
            
            if (r, c) in visited:     # ignore duplicates
                continue
            
            area += 1
            visited.add((r, c))
            temp_visited.add((r, c))
            
            for dr, dc in [[1,0], [-1, 0], [0, 1], [0, -1]]:
                row = dr + r
                col = dc + c
                
                # if row >= 0 and row < ROWS and col >= 0 and col < COLS and (row, col) not in visited and grid[row][col]
                
                if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visited or grid[row][col] == 0:
                    continue
                
                # visited.add((r, c))
                stack.append((row, col))
                
        island_area[island_count] = area
        
        for r, c in temp_visited:
            coordinates_island[(r, c)] = island_count
        
        island_count += 1
    
    for i in range(ROWS):
        for j in range(COLS):
            # print('visited',visited)
            if (i, j) not in visited and grid[i][j] == 1:
                dfs(i, j)
                
    res = 0
                
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                island_id = coordinates_island[(i, j)]
                area = island_area[island_id]
                res = max(res, area)
            else:
                islands = set()
                
                for dr, dc in [[1,0], [-1, 0], [0, 1], [0, -1]]:
                    row = dr + i
                    col = dc + j

                    if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                        continue
                        
                    if grid[row][col] == 1:
                        islands.add(coordinates_island[(row, col)])
                
                total_area = 1
                for k in islands:
                    total_area += island_area[k]
                
                res = max(res, total_area)
                    
    print(island_area)
    print(coordinates_island)
    print(res)
    return res
    
    
# grid = [
#     [0,1,1,0,0],
#     [1,1,0,0,1],
#     [0,0,0,0,0],
# ]
# grid = [[1,0],[0,1]]
# grid = [[1,1],[1,0]]x
grid = [
    [1,1],
    [1,1]
]
largestIsland(grid)