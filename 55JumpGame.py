class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = j = 0
        while i <= j:
            j = max(i+nums[i], j)
            if j>=len(nums)-1:
                return True
            i +=1
        return False