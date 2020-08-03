"""
Binary Search:
[1,1,2,3,3,4,4,8,8]
if i is even:
    for all i before single number：
        nums[i] == nums[i+1]
    for all i after single number:
        nums[i] == nums[i-1]
mid will only appear on even index and first nums[i]!=nums[i+1]

"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        l = 0
        r = len(nums)-1
        while l < r:
            mid = 2*((r+l)//4) # mid is even
            if nums[mid]==nums[mid+1]:
                l = mid +2
            else:
                r = mid # mid might be single number
        return nums[r]