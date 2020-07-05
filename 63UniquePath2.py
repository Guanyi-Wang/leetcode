from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        num_row = len(obstacleGrid)
        num_col = len(obstacleGrid[0])
        ans = [[0]*num_col for _ in range(num_row)]
        ans[0][0] = 1
        for i in range(1,num_row):  # define first column
            if not obstacleGrid[i][0]:
                ans[i][0] = ans[i-1][0]
        # print(ans)
        for i in range(1,num_col):  # define first row
            if not obstacleGrid[0][i]:
                ans[0][i] = ans[0][i-1]
        # print(ans)
        for r in range(1,num_row):
            for c in range(1,num_col):
                if obstacleGrid[r][c] == 1:
                    continue  # ans = 0
                else:
                    ans[r][c] = ans[r-1][c] + ans[r][c-1]
        # print(ans)
        return ans[-1][-1]