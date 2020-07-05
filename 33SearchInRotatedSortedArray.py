from typing import List
"""
Binary Search method
1. find the mid, seperate the list into two.
2. One of these two part must be monotonous increasing, find this one.
3. Do binary search on this part.
4. If not in this part, drop this part and do step 1 on the other part.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:  # == should be included [2,1] 1
                if nums[low] <= target and target < nums[mid]:  # target in this part
                    high = mid - 1
                else:  # target not in this part, drop left part
                    low = mid + 1
            else:  # right part is monotonic
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

