"""
Use solution from 198.
find max from nums[1] to nums[-2]
for nums[0] and nums[-1], there are 3 situations:
both not rob (wont be max solution)
rob 0
rob -1
final solution is the max of those two.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        def rob_helper(start, end):
            dp_i2 = 0
            dp_i0 = 0
            dp_i1 = 0
            for i in range(start, end+1):
                dp_i2 = max(dp_i1, dp_i0+nums[i])
                dp_i0 = dp_i1
                dp_i1 = dp_i2
            return dp_i2
        return max(rob_helper(1,len(nums)-1), rob_helper(0,len(nums)-2))