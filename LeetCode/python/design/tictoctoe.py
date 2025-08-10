		
class TicTacToe:
    def __init__(self, n):
        self.rows = [0 * n]
        self.cols = [0 * n]
        self.mainDiag = 0
        self.diag = 0
        self.n = n
        
    def move(self, row, col, player):
        score = 1 if player == 1 else -1
        self.rows[row] += score
        self.cols[col] += score
        
        if row == col:
            self.mainDiag += score
        
        if row + col == self.n - 1:
            self.diag += score
        
        if score * self.n in [self.rows[row], self.cols[col], self.mainDiag, self.diag]:
            return player
        
        return 0
        
        

# player is either 1 or 2
# 1 is plus 1
# 2 is minus 1

# increase or decrease each turn
# if any turn there is a target score either n or -n return the player
# important part: to determine main diag: col == row
# to determine sideDiag: col + row == n - 1 where n is size of the matrix
