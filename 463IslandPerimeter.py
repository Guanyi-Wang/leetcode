class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        peri = 0
        row = 0
        col = 0
        # find start island
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    row = r
                    col = c
        visited = {}

        def dfs(row, col):
            if (row, col) in visited:
                return 0
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
                return 1
            if grid[row][col] == 0:
                return 1
            peri = 0
            visited[(row, col)] = 1
            peri += dfs(row - 1, col)
            peri += dfs(row + 1, col)
            peri += dfs(row, col - 1)
            peri += dfs(row, col + 1)
            return peri

        return dfs(row, col)
