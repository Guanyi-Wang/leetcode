from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        res = [[0]*n for _ in range(n)]
        direction = [[0,1], [1,0], [0,-1], [-1,0]]
        d = 0
        ri = ci = 0
        for i in range(n*n):
            res[ri][ci] = i+1
            r = ri+direction[d][0]
            c = ci+direction[d][1]
            if 0<=r<n and 0<=c<n and res[r][c] == 0:
                ri = r
                ci = c
            else:
                d = (d+1)%4
                ri += direction[d][0]
                ci += direction[d][1]
        return res