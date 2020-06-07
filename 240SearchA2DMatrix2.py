class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        for i in matrix:
            if target < i[0]:
                return False
            if target > i[-1]:
                continue
            else:
                flag = self.binarySearch(i, target)
                if flag:
                    return True
        return False

    def binarySearch(self, i, target):
        start = 0
        end = len(i) - 1
        while start <= end:
            mid = end + (start - end) // 2
            if target == i[mid]:
                return 1
            elif target < i[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return 0
