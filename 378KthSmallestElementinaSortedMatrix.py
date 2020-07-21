class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix):
            hp = [(matrix[0][0], 0, 0)]
            visited = {(0, 0):1}
            for _ in range(k-1):
                _, row, col = heapq.heappop(hp)
                if row+1<len(matrix) and (row+1, col) not in visited:
                    heapq.heappush(hp, (matrix[row+1][col], row+1, col))
                    visited[(row+1, col)] = 1
                if col+1<len(matrix) and (row, col+1) not in visited:
                    heapq.heappush(hp, (matrix[row][col+1], row, col+1))
                    visited[(row, col+1)] = 1
            res,_, _ = heapq.heappop(hp)
            return res