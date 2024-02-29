from queue import Queue
from collections import deque
def orangesRotting(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    freshOranges = 0
    q = Queue()
    time = 0
    DIRECTIONS = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1),
    ]  

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 2:
                q.put((i,j))
                # q.append((i,j))
            if grid[i][j] == 1:
                freshOranges += 1
    
    while not q.empty():
    # while q:
        for _ in range(q.qsize()):
        # for _ in range(len(q)):
            # u = q.pop()
            u = q.get()
            print(u[0], u[1])
            for dr, dc in DIRECTIONS:
                r = dr + u[0]
                c = dc + u[1]
                if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
                    grid[r][c] = 2
                    q.put((r,c))
                    # q.append((r,c))
                    freshOranges -= 1
                    
        time += 1
        print('=================')
    return time if freshOranges == 0 else -1
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
print(orangesRotting(grid))
# Get all fresh oranges

# Get all rotten oranges put into Q

# While loop stops when running out of fresh oranges or Queue empty

    # Run all rotten oranges at the same time by for loop

        # For each rotten oranges, mark adjacent fresh oranges rotten
        
        # Put newly rotten oranges into Q
    
    # Increase time by one after running through for 

# if fresh oranges > 0 then impossible else return imposible    