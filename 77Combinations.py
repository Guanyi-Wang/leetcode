from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n or not k:
            return []
        nums = [i for i in range(1, n + 1)]
        res = []
        self.backTrack(nums, 0, [], res, k)
        return res

    def backTrack(self, nums, start, temp, res, k):
        if len(temp) == k:
            res.append(temp)
            return
        for i in range(start, len(nums)):
            self.backTrack(nums, i + 1, temp + [nums[i]], res, k)
