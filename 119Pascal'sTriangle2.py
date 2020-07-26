"""
Dynamic Programming
generate new rows from end to start, because row[n] = row[n]+row[n-1], from start to end will change row[n-1]
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = rowIndex+1
        row = r*[1]
        for i in range(r):
            for j in range(i-1, 0, -1):
                row[j] += row[j-1]
        return row