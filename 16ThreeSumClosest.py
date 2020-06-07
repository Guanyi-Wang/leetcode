from typing import List
"""
Two pointers
O(NlogN+N**2) O(1)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = sum(nums[:3])
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s - target) < abs(res - target):  # dont need to move pointers here
                    res = s
                if s > target:
                    r -= 1
                if s < target:
                    l += 1
        return res


