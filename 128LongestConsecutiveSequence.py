"""
Keep all nums in hash table.
Only count from the start of the susequence.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        for n in nums:
            dict[n] = 1
        res = 0
        for n in dict:
            if n-1  not in  dict:
                cur = n
                cur_max = 0
                while cur in dict:
                    cur+=1
                    cur_max+=1
                res = max(res, cur_max)
        return res