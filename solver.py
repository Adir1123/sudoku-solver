class Solver:
    def __init__(self, board):
        self.board = board


    def is_valid_move(self, row, col, num):

        #checks row and cols
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        row_corner = row - (row % 3)
        col_corner = col - (col % 3)

        #checks every 3x3 block starting from his corner
        for i in range(3):
            for j in range(3):
                if self.board[row_corner + i][col_corner + j] == num:
                    return False
        return True



    def solve(self, row=0, col=0):
        if row == 9:
            return True
        elif col == 9:
            return self.solve(row + 1, col=0)
        elif self.board[row][col] != 0:
            return self.solve(row, col + 1)
        else:
            for i in range(1,10):
               if self.is_valid_move(row,col,i):

                   self.board[row][col] = i

                   if self.solve(row,col+1): # move to the next cell and returns true if we found a solution
                       return True
                   else:
                       self.board[row][col] = 0 # undo move

            return False # no solution