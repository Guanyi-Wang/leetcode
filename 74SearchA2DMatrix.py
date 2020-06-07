class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row_len = len(matrix[0])
        num_row = len(matrix)
        start = 0
        end = row_len*num_row-1
        while start <= end:
            mid = (end+start)//2
            num = matrix[mid//row_len][mid%row_len]
            print(num)
            if num == target:
                return True
            elif num < target:
                start = mid + 1
            else:
                end = mid-1
        return False