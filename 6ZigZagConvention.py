"""
Every numRows + 1 is a pattern.
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or len(s) == 1:
            return s
        if numRows == 1:
            return s
        #  create list to store output
        res = [''] * numRows
        ind = -1
        direction = 1
        for i, ch in enumerate(s):
            if i == 0:
                ind += direction
                res[ind] += ch
            elif i % (numRows - 1) == 0:
                ind += direction
                res[ind] += ch
                direction = -direction
            else:
                ind += direction
                res[ind] += ch

        return ''.join(res)

