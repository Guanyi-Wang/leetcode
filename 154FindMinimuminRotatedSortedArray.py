"""
Divide and Conqure
keep seperating nums into two. find the min of smaller list.
if smaller list is sorted, nums[l]<nums[r],return nums[l] and because of this,
time complexity is better than O(N)
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None

        def dC(l, r):
            if r - l <= 1:
                return min(nums[l], nums[r])
            # if sorted, min is nums[l]
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r) // 2
            return min(dC(l, mid - 1), dC(mid, r))

        return dC(0, len(nums) - 1)
