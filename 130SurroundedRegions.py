"""
Find all O on the edge. Find all O connected to them (BFS)and mark them as A. Go through matrix again and mark all O(O not connected to the edge) to X and A to O.
"""
from  typing import List
import collections

"""
Find all O on the edge. Find all O connected to them (BFS)and mark them as A. Go through matrix again and mark all O(O not connected to the edge) to X and A to O.
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        num_row = len(board)
        num_col = len(board[0])
        for r in range(num_row):
            for c in range(num_col):
                if r == 0 or r ==num_row-1 or c == 0 or c == num_col-1:
                    if board[r][c] == 'O':
                        print([r,c])
                        self.bfs(board,r,c)
        for r in range(num_row):
            for c in range(num_col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'A':
                    board[r][c] = 'O'
    def bfs(self, board, r,c):
        dq = collections.deque([(r,c)])
        while dq:
            row, col = dq.popleft()
            if 0<=row<len(board) and 0<=col<len(board[0]) and board[row][col] == 'O':
                board[row][col] = 'A'
                dq.extend([(row-1,col),(row,col-1),(row+1, col), (row, col+1)])
