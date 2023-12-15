from queue import Queue

directions = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)    
]

def solve(board):
    row = len(board)
    col = len(board[0])
    visited = [[True] * col for i in range(row)] 
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O':
                visited[i][j] = False
    # for v in visited:
    #         print(v)
    for i in range(row):
        for j in range(col): 
            if not visited[i][j]:
                areas = []
                q = Queue()
                q.put((i, j))
                areas.append((i,j))
                visited[i][j] = True
                while not q.empty():
                    ir, jc = q.get()
                    for dr, dc in directions:
                        nearR = ir + dr
                        nearC = jc + dc
                        if 0 <= nearC < col and 0 <= nearR < row and not visited[nearR][nearC]:
                            print(nearR, nearC)
                            visited[nearR][nearC] = True
                            q.put((nearR, nearC))
                            areas.append((nearR, nearC))          
                # get neighbors of areas
                # if neighbors outbound continue for loop
                neighbors = []
                outbound = False
                for xr,yc in areas:
                    for dr, dc in directions:
                        sumr = xr + dr
                        sumc = yc + dc
                        if sumc < 0 or sumc >= col or sumr < 0 or sumr >= row:
                            outbound = True
                if not outbound:
                    for xr,yc in areas:
                        board[xr][yc] = 'X'
    
    # for b in board:
    #     print(b)             
board = [
    ["X","O","X","O","X","O"],
    ["O","X","O","X","O","X"],
    ["X","O","X","O","X","O"],
    ["O","X","O","X","O","X"]
]
# board = [["X"]]
solve(board)