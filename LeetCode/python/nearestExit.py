from queue import Queue

def nearestExit(maze, entrance):
    ROWS = len(maze)
    COLS = len(maze[0])
    DIRECTIONS = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1),
    ]    
    visited = [[False for i in range(COLS)] for j in range(ROWS)]

    q = Queue()
    q.put([entrance[0], entrance[1], 0])
    visited[entrance[0]][entrance[1]] = True
    
    while not q.empty():
        u = q.get()
        for r, c in DIRECTIONS:
            vr = u[0] + r            
            vc = u[1] + c            
            if 0 <= vr < ROWS and 0 <= vc < COLS and not visited[vr][vc] and maze[vr][vc] == '.':
                visited[vr][vc] = True
                q.put([vr, vc, u[2] + 1])
                
            # # exclude 
            if u[0] == entrance[0] and u[1] == entrance[1]:
                continue
            
            if vr < 0 or vr >= ROWS or vc < 0 or vc >= COLS:
                return u[2]
                
    return -1

maze = [[".","+"]]
entrance = [0,0]
print(nearestExit(maze,entrance))

