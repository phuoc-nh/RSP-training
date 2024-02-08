def exist(board, word):
    ROWS = len(board)
    COLS = len(board[0])
    visited = set()
    def dfs(i, r, c):
        if i == len(word):
            return True
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i] or (r, c) in visited:
            return False

        visited.add((r, c))
        print(i, r, c)
        res = dfs(i+1, r+1, c) or dfs(i+1, r-1, c) or dfs(i+1, r, c+1) or dfs(i+1, r, c-1)        

        visited.remove((r, c))
        return res
    
    for i in range(ROWS):
        for j in range(COLS):
            if dfs(0, i, j):
                return  True
    
    return False

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]]
word = "SEE"

print(exist(board, word))
# O(n*m*4^len(word))