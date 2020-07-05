from typing import List

"""
find the largest of two and put it at the end of nums1.
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        k = m + n - 1  # index of last digit
        m -= 1
        n -= 1
        while n >= 0:
            if m < 0:  # nums1 all in position, put nums left in nums2 at the start of nums1
                while n >= 0:
                    nums1[k] = nums2[n]
                    k -= 1
                    n -= 1
                return
            if nums1[m] >= nums2[n]:  # find the max from end of both list
                nums1[k] = nums1[m]
                k -= 1
                m -= 1
            else:
                nums1[k] = nums2[n]
                k -= 1
                n -= 1

