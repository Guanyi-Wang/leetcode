from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return None
        res = []
        candidates.sort()
        self.backtrace(candidates,[], target, 0,res)
        return res
    def backtrace(self, candidates,temp, remain, start,res):
        if remain < 0:
            return
        elif remain == 0:
            res.append(temp)
        else: #  remain > 0
            for i in range(start, len(candidates)):
                self.backtrace(candidates, temp + [candidates[i]], remain - candidates[i], i, res)# when remain <=0, no solution or solution updated

print(Solution().combinationSum([2,3,6,7], 7))
#
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         if not candidates:
#             return None
#         res = []
#         candidates.sort()
#         self.backtrace(candidates,[], target, 0,res)
#         return res
#     def backtrace(self, candidates,temp, remain, start,res):
#         if remain < 0:
#             return
#         elif remain == 0:
#             res.append(temp)
#         else: #  remain > 0
#             for i in range(start, len(candidates)):
#                 self.backtrace(candidates, temp+[candidates[i]], remain-candidates[i], i,res)# when remain <=0, no solution or solution updated