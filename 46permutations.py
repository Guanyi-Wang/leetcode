from typing import List
"""
Backtrace
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 0
        temp = []
        ans = []
        self.pR(nums, temp, ans)
        return ans

    def pR(self, nums: List[int], temp: List[int], ans=[List[int]]):
        if len(temp) == len(nums):
            ans.append(temp[:])
        else:
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                else:
                    temp.append(nums[i])
                    self.pR(nums, temp, ans)
                    temp.pop()

    """
    Use swap. 
    """

    class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:
            if not nums:
                return 0
            temp = []
            ans = []
            self.pR(nums, 0, ans)
            return ans

        def pR(self, nums: List[int], start: int, ans=[List[int]]):
            if start == len(nums) - 1:
                ans.append(nums[:])
            else:
                for i in range(start, len(nums)):
                    nums[i], nums[start] = nums[start], nums[i]  # swap from start
                    self.pR(nums, start + 1, ans)
                    nums[i], nums[start] = nums[start], nums[i]  # swap back