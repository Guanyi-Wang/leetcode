from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in board:
            dic = {}
            for ch in row:
                if not ch == '.':
                    if ch in dic:
                        return False
                    else:
                        dic[ch] = 1
        # check column
        for col in range(9):
            dic = {}
            for row in range(9):
                ch = board[row][col]
                if not ch =='.':
                    if ch in dic:
                        return False
                    else:
                        dic[ch] = 1
        # check sub-box
        for row in range(0,9,3):
            for col in range(0,9,3):
                dic = {}
                for i in range(3):
                    for j in range(3):
                        ch = board[row+i][col+j]
                        if not ch == '.':
                            if ch in dic:
                                return False
                            else:
                                dic[ch] = 1
        return True

    class Solution:
        def isValidSudoku(self, board: List[List[str]]) -> bool:
            dic = {}
            for row in range(9):
                for col in range(9):
                    ch = board[row][col]
                    if not ch == '.':
                        if not ch + ' in row' + str(row) in dic and not ch + ' in col ' + str(
                                col) in dic and not ch + ' in sub-box' + str(row // 3) + str(col // 3) in dic:
                            dic[ch + ' in row' + str(row)], dic[ch + ' in col ' + str(col)], dic[
                                ch + ' in sub-box' + str(row // 3) + str(col // 3)] = 1, 1, 1
                        else:
                            return False
            return True


