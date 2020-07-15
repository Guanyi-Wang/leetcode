"""
Recursive function, find all permutations of nums and results.
"""
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) ==1:
            return abs(nums[0]- 24)<0.001
        else:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    temp = nums[:i]+nums[i+1:j]+nums[j+1:]
                    if self.judgePoint24(temp+[nums[i]+nums[j]]) or self.judgePoint24(temp+[nums[i]-nums[j]]) or self.judgePoint24(temp+[nums[i]*nums[j]]) or self.judgePoint24(temp+[nums[j] and nums[i]/nums[j]])or self.judgePoint24(temp+[nums[i] and nums[j]/nums[i]])or self.judgePoint24(temp+[nums[j] and nums[j]-nums[i]]):
                        return True
            return False