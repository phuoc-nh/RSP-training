def solveNQueens(n: int):
    board = [['.'] * n for i in range(n)]
    # print(board)
    # board[0][0] = 'Q'
    # for b in board:
    #     print(b)
    
    
            
    def inbound(r, c):
        if r < 0 or c < 0 or r >= n or c >= n:
            return False
        
        return True 
    
    def canPlaceQ(i, j):
        print('i, j', i, j)
        for b in board:
            print(b.copy())
        # check row
        for k in range(n):
            if k == j:
                continue
            
            if board[i][k] == 'Q':
                print('row', i, k)
                return False
        
        # check column
        for k in range(n):
            if k == i:
                continue
            if board[k][j] == 'Q':
                print('col', k, j)
                return False
        
        # check diagonal 
        r = i
        c = j
        while inbound(r, c):
            if r == i and c == j:
                r += 1
                c += 1
                continue
            
            if board[r][c] == 'Q':
                return False
            
            r += 1
            c += 1

        r = i
        c = j
        while inbound(r, c):
            if r == i and c == j:
                r -= 1
                c += 1
                continue
            
            if board[r][c] == 'Q':
                return False
            
            r -= 1
            c += 1
        
        r = i
        c = j
        while inbound(r, c):
            if r == i and c == j:
                r += 1
                c -= 1
                continue
            
            if board[r][c] == 'Q':
                return False
            
            r += 1
            c -= 1
        
        r = i
        c = j
        while inbound(r, c):
            if r == i and c == j:
                r -= 1
                c -= 1
                continue
            
            if board[r][c] == 'Q':
                return False
            
            r -= 1
            c -= 1

        return True
    
    res = []
        
    def backtrack(r):
        if r >= n:
            # done and print current board
            print('board', board)
            res.append([''.join(b) for b in board])
            return 
        for c in range(n):
            could = canPlaceQ(r, c)
            print('could', could, r, c)
            if could:
                board[r][c] = 'Q'
                backtrack(r + 1)
                board[r][c] = '.'
                
    backtrack(0)
    # board = [
    #     ['Q', '.', '.', '.'],
    #     ['.', '.', '.', '.'],
    #     ['.', '.', '.', '.'],
    #     ['.', '.', '.', '.'],
    # ]
    # print('>>>', canPlaceQ(3, 0))
    
    
    return res
        
        

n = 4

res = solveNQueens(n)
print('res', res)