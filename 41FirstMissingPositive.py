"""
O(n) time and O(1) space Solution.
Most important observation for this problem:
The first missing positive number must be in range of [1,len(nums)].
Because list nums can only contain at most len(nums) continous positive integers.
So it's possible to iterate over nums and put num in range of [1, len(nums)] in nums[num-1] and ignore others.
Finally iterate over nums again to find the first num+1 != nums[num]
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # first iteration to put num in [1, len(nums)] in correct location
        for i in range(len(nums)):
            while 1<=nums[i]<=len(nums) and nums[nums[i]-1]!= nums[i]: # keep swapping till num not in range or num = i
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        # second iteration to find the first
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        # if not return before this, nums contains 1~len(nums), so return len(nums)+1
        return len(nums)+1