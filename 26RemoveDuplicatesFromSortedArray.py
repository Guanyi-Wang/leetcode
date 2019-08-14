from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        for i in range(len(nums)):
            if nums[i]!=nums[count]:
                count += 1
                nums[count] = nums[i]
        nums = nums[:count+1]
        return count+1
    