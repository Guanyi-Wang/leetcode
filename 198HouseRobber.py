"""
top down DP with mem
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mem = [-1]*len(nums)
        def dp(nums, start):
            if start >= len(nums):
                return 0
            if mem[start]==-1:
                mem[start] =  max(dp(nums, start+1), nums[start]+dp(nums, start+2))
            return mem[start]
        return dp(nums, 0)

"""
Bottom up DP
dp[i] = max(dp[i-1], dp[i-2]+nums[i])
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [-1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[0]
            elif i == 1:
                dp[i] = max(nums[:2])
            else:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

"""
Bottom up DP
dp[i] = max(dp[i-1], dp[i-2]+nums[i])
space optimization
dp_i2 = max(dp_i1, dp_i0+nums[i])
dp_i0 = dp_i1
dp_i1 = dp_i2
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp_i2 = 0
        dp_i0 = 0
        dp_i1 = 0
        for i in range(len(nums)):
            dp_i2 = max(dp_i1, dp_i0+nums[i])
            dp_i0 = dp_i1
            dp_i1 = dp_i2
        return dp_i2