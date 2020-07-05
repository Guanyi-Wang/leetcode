from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        for r in range(num_row):
            for c in range(num_col):
                if r == 0 and c == 0:
                    continue  # skip grid[0][0]
                elif r == 0:  # first row
                    grid[r][c] += grid[r][c-1]
                elif c == 0:   # first col
                    grid[r][c] += grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        # print(grid)
        return grid[-1][-1]