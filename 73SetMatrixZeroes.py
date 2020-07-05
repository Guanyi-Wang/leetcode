"""
Iterate over matrix, set matrix[i][0] = matrix[0][j] if matrix[i][j] == 0 as a flag.
Notice that matrix[0][0] is special because it's the start of first row and col. Here we use it to store the flag of first row and we use additional variable for first column
Iterate again from second row and col to change value because the flags should not be modified during the iteration.
Finally check the matrix[0][0] to modify the first col and row

"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_col = 1
        for i in range(len(matrix)):
            if matrix[i][0] == 0:  # If there is any 0 in first col
                first_col = 0
            for j in range(1, len(matrix[0])):  # dont forget to skip first col
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if not matrix[0][0]:  # flag of first row
            matrix[0] = [0] * len(matrix[0])
        if not first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
