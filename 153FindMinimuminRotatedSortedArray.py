"""
Modified version of Binary Search
eg:[6,7,1,2,3,4,5]
    l     m     r
    nums[2] is min, nums[2]< both nums[2-1] and nums[2+1] -> return condition.
    start from:
    nums[mid] =2 < nums[0] -> min in [l, m-1] - > r = mid-1
    or if nums[mid] > nums[0] eg. mid = 1
    l = mid+1

"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if nums[-1] >= nums[0]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
