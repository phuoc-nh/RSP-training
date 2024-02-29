
def solve(board):
    ROWS, COLS = len(board), len(board[0])

    def dfs(r, c):
        # base case
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
            return
        
        board[r][c] = 'T'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
            
    for i in range(ROWS):
        for j in range(COLS):
            if (i in [0, ROWS-1] or j in [0, COLS-1]) and board[i][j] == 'O':
                dfs(i, j)
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'T':
                board[i][j] = 'O'
    for b in board:
        print(b)
board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]

solve(board)