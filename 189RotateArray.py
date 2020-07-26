from typing import List

"""
Reverse Three times:
for a given length n nums: [1,2,3,4,5,6,7] k=3
1. reverse entire nums[7,6,5,4,3,2,1]
2. reverse first k elements[5,6,7,4,3,2,1]
3. reverse the rest  elements[5,6,7,1,2,3,4]
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)



