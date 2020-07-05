"""
Use recursion. Two kinds of solutions for each case: either take this coin or skip this coin and go on.
Base case:
remain == 0, find one solution
remain < 0, wrong solution, already exceeded
i == len(coins), reach the last coin

"""
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.changeRecursion(amount, 0, coins)

    def changeRecursion(self, remain, i, coins):
        if remain == 0:
            return 1
        if remain < 0 or i == len(coins):
            return 0
        # either choose this coins or skip
        return self.changeRecursion(remain - coins[i], i, coins) + self.changeRecursion(remain, i + 1, coins)


"""
Top down dp
Based on previous solution, use dp[][] to store replicated results during recursion.
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * len(coins) for _ in range(amount + 1)]
        return self.changeRecursion(amount, 0, coins, dp)

    def changeRecursion(self, remain, i, coins, dp):
        if remain == 0:
            return 1
        if remain < 0 or i == len(coins):
            return 0
        if dp[remain][i] != -1:
            return dp[remain][i]
        # either choose this coins or skip
        dp[remain][i] = self.changeRecursion(remain - coins[i], i, coins, dp) + self.changeRecursion(remain, i + 1,
                                                                                                     coins, dp)
        return dp[remain][i]

"""
Bottom up
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        dp[0][0] = 1
        for i in range(1,len(coins)+1):
            for j in range(amount+1):
                if j - coins[i-1] < 0:
                    dp[i][j] = dp[i-1][j] # cant take the last coin
                else:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
        return dp[-1][-1]

"""
    moemorization used, top down
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        if m==1 or n ==1:
            return 1
        ans = [[-1]*n for _ in range(m)]
        self.backTrack(m,n,0,0,ans)
        return ans[0][0]
    def backTrack(self, m, n, row, col, ans):
        if row >= m or col >=n:
            return 0
        if ans[row][col] != -1:
            return ans[row][col]
        if row == m-1 and col == n-1:
            return 1
        ans[row][col] = self.backTrack(m,n,row+1,col,ans)+self.backTrack(m,n,row,col+1,ans)
        return ans[row][col]

"""
Top down
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        if m == 1 or n == 1:
            return 1
        ans = [[0] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if i == 0 or j == 0:  # only one way to go straight
                    ans[i][j] = 1
                else:
                    ans[i][j] = ans[i - 1][j] + ans[i][j - 1]
        return ans[-1][-1]

"""
One dimension space
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        if m==1 or n ==1:
            return 1
        ans = [1]*m
        for i in range(1,n):
            for j in range(1,m):
                if i==0 or j==0:  # only one way to go straight
                    ans[j] = 1
                else:
                    ans[j] = ans[j]+ans[j-1]
        return ans[-1]

