class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return None
        nums.sort()
        res = []
        temp = []
        self.pUR(nums, temp, res)
        return res
    def pUR(self, nums,temp,res):
        if not nums:
            res.append(temp[:])
        else:
            for i in range(len(nums)):
                if i> 0  and nums[i-1] == nums[i]:
                    continue
                self.pUR(nums[:i]+nums[i+1:], temp+[nums[i]], res)
