from typing import List
"""
Dynamic Programming
if a%b==0 and c%b==0, then c%a==0
Sort the nums and keep track of all nums before index i which meet the condition: nums[i]%nums[i-n]==0.
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = []
        nums.sort()  # put divisor before dividend
        subsets = [[n] for n in nums]  # list to store subsets of nums meet the condition. initail as [[1],[2],[3]]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(subsets[i])< len(subsets[j])+1:
                    subsets[i] = [nums[i]] + subsets[j] # find the max among all nums meet the condition
        return max(subsets, key = len)