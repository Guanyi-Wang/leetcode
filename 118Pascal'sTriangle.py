class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for r in range(numRows):
            row = []
            for i in range(r + 1):
                if i == 0 or i == r:
                    row.append(1)
                else:
                    row.append(tri[r - 1][i - 1] + tri[r - 1][i])
            tri.append(row)
        return tri
