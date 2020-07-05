from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        reverse then transpose
        """
        matrix[:] = zip(*matrix[::-1])