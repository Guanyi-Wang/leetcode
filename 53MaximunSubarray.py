from typing import List


# Brute force O(n**2) O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        for i in range(len(nums)):
            sum = nums[i]
            maxi = max(maxi, sum)  # in case the last digit itself is largest, like[-1,2]
            for j in range(i + 1, len(nums)):
                sum = nums[j] + sum
                maxi = max(maxi, sum)
        return maxi

# Dynamic programming O(n) O(1)
"""
loc_max[i]  is continuous max end with i  which means i must be included
so loc_max[i] = max(loc_max[i]+nums[i], nums[i]), either start a new max or add with previous
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        loc_max = glob_max = nums[0]
        for i in range(1, len(nums)):
            loc_max = max(nums[i], loc_max + nums[i])
            glob_max = max(loc_max, glob_max)
        return glob_max
