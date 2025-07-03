import heapq
def minimumEffortPath(heights) -> int:
    ROWS = len(heights)
    COLS = len(heights[0])

    heap = [(0, 0, 0)]
    visited = set((0, 0))

    while len(heap):
        r, c, effort = heapq.heappop(heap)
        
        # if (r, c) in visited:
        #     continue
        
        # visited.add((r, c))
        
        if r == ROWS - 1 and c == COLS - 1:
            print('eff', effort)
            return effort
        
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0,-1]]:
            row = dr + r
            col = dc + c
            
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visited:
                continue
            visited.add((r, c))
            # keep track the max effort along the way by comparing the next effort and cur effort
            maxEffort = max(effort, abs(heights[r][c] - heights[row][col]))
            heapq.heappush(heap, (row, col, maxEffort))
    
            
    return 1

heights = [[1,2,2],[3,8,2],[5,3,5]]
minimumEffortPath(heights)