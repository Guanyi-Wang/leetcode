"""
Linear:
nums[-1]< nums[0], so the nums is ascending in the beginning,  we need to return the item before
descending or the last item since nums[n] = -inf.
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] >nums[i+1]:
                return i
        return len(nums)-1

"""
Binary Search:
nums[-1]< nums[0], so the nums is ascending in the beginning, if nums[mid]>nums[mid+1], mid in descending part, peak on the left of mid,  r = mid. else mid in ascending part, peak on the right of mid.
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid +1
        return l