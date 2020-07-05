import collections
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return res.values()