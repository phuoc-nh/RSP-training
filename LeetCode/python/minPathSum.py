class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                    continue
                
                if j == 0:
                    grid[i][j] += grid[i-1][j]
                    continue

                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        ROWS = len(grid)
        COLS = len(grid[0])
        print(grid)
        return grid[ROWS-1][COLS-1]

        # ROWS = len(grid)
        # COLS = len(grid[0])
        # queue = [(grid[0][0], 0, 0)]
        # res = 0
        # visited = set()
        # while len(queue):
        #     w, r, c = heapq.heappop(queue)
        #     if (r, c) in visited:
        #         continue

        #     res = w
        #     visited.add((r, c))

        #     if r == ROWS - 1 and c == COLS - 1:
        #         return res

        #     for dr, dc in [[0, 1], [1, 0]]:
        #         row = r + dr
        #         col = c + dc
        #         if row >= ROWS or col >= COLS or (row, col) in visited:
        #             continue
                
        #         heapq.heappush(queue, (w + grid[row][col], row, col))

        # return 0
