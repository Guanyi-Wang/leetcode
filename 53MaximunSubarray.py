from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        loc_max = glob_max = nums[0]
        for i in range(1, len(nums)):
            loc_max = max(nums[i], loc_max + nums[i])
            glob_max = max(loc_max, glob_max)
        return glob_max
