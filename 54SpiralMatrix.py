from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return None
        res = []
        num_row = len(matrix)
        num_col = len(matrix[0])
        seen = [[0]*num_col for _ in matrix]
        direction = [[0,1], [1,0], [0,-1], [-1,0]] # four ways of change index
        d = 0 # dirction indicator
        ri = ci = r = c = 0  # current index for rows and cols
        for i in range(num_row*num_col):
            res.append(matrix[ri][ci])
            seen[ri][ci] = 1
            r =ri+ direction[d][0]
            c =ci+ direction[d][1]
            if 0<=r < num_row and 0<=c < num_col and not seen[r][c]:
                ri = r
                ci  = c
            else:
                d = (d+1)%4
                ri += direction[d][0]
                ci += direction[d][1]
        return res