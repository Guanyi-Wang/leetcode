from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ans = [[]]
        for num in nums:
            ans+=[i + [num] for i in ans]
        return ans


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ans = []

        def backTrack(nums, temp):
            if len(temp) <= len(nums):
                ans.append(temp[:])
            for i in range(len(nums)):
                backTrack(nums[i + 1:], temp + [nums[i]])

        backTrack(nums, [])
        return ans