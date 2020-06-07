from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        # find empty cells
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    #  Try solutions from '1' to '9'
                    sol = '1'
                    while int(sol) <= 9:
                        if self.isValid(i, j, sol):
                            self.board[i][j] = sol  # find next empty and do above
                            # check if next cell has a solution
                            if self.solveSudoku(self.board):
                                return True
                            else:
                                self.board[i][j] = '.'  # reset this one
                        sol = str(int(sol) + 1)
                    return False  # if sol > 10 which means no solution for this cell
        return True  # if we complete all, we need to return true to previous call

    def isValid(self, i, j, sol):
        # check row
        for _ in range(9):
            ch = self.board[i][_]
            if ch == sol:
                return False
        # check column
        for _ in range(9):
            ch = self.board[_][j]
            if ch == sol:
                return False
        # check sub-box
        i = i // 3 * 3
        j = j // 3 * 3
        for m in range(3):
            for n in range(3):
                ch = self.board[i + m][j + n]
                if ch == sol:
                    return False
        return True

