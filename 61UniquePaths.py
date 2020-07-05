"""
DP, TLE
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        if m==1 or n ==1:
            return 1
        ans = self.backTrack(m,n,0,0)
        return ans
    def backTrack(self, m, n, row, col):
        if row > m or col >n:
            return 0
        if row == m-1 and col == n-1:
            return 1
        return self.backTrack(m,n,row+1,col)+self.backTrack(m,n,row,col+1)