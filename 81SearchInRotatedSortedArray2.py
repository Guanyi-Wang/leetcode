from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            while left < mid and nums[left] == nums[mid]:  # avoid dupulicates[1,3,1,1,1]
                left += 1
            if nums[left] <= nums[mid]:  # left part is sorted
                if target >= nums[left] and target < nums[mid]:  # target in left sorted part
                    right = mid - 1  # drop right part
                else:  # target not in the left sorted part
                    left = mid + 1  # drop left part
            else:  # left part is not sorted so right part must be sorted
                if target > nums[mid] and target <= nums[right]:  # target in right sorted part
                    left = mid + 1  # drop left part
                else:  # target in left unsorted part
                    right = mid - 1
        return False
