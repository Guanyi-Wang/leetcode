from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:  # find the first descending pair
            i -= 1
        if i == 0:
            nums = nums.reverse()
            return
        i -= 1
        j = len(nums) - 1
        while j > 0 and nums[j] <= nums[i]:  # find the first ascending
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]  # swap
        #  reverse the [i+1:]
        l = i + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
