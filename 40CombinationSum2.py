from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return None
        candidates.sort()
        res = []
        temp = []
        self.cR2(candidates, temp, target, res)
        return res

    def cR2(self, candidates, temp, remain, res):
        if remain == 0:
            res.append(temp)
            return
        elif remain < 0:
            return
        else:
            for i in range(len(candidates)):
                if i > 0 and candidates[i - 1] == candidates[i]:
                    continue
                self.cR2(candidates[i + 1:], temp + [candidates[i]], remain - candidates[i], res)