class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        res = []
        start = 0
        end = len(nums) - 1
        #  find the left most target
        while start <= end:
            mid = (start+end)//2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        if start == len(nums) or nums[start] != target:  # there is no target in the list
            return [-1, -1]
        else:
            res.append(start)
        start = 0
        end = len(nums) - 1
       #  find the right most target
        while start <= end:
            mid = (start+end)//2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        res.append(end)
        return res