def isValidSudoku(board) -> bool:
    
    # check row 
    for i in range(9):
        rowSet = set()
        for j in range(9):
            char = board[i][j]
            if char == '.':
                continue
            
            if char in rowSet:
                return False
            else:
                rowSet.add(char)
    print('row')  
    # check col
    for i in range(9):
        colSet = set()
        for j in range(9):
            char = board[j][i]
            if char == '.':
                continue
            if char in colSet:
                return False
            else:
                colSet.add(char)
    print('col')    
    # check sub box 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            boxSet = set()
            
            for k in range(i, i+3):
                for l in range(j, j + 3):
                    char = board[k][l]
                    if char == '.':
                        continue
                    if char in boxSet:
                        return False
                    else:
                        boxSet.add(char)

    return True
    
    
    
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

res = isValidSudoku(board)
print(res)
