import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        counts = collections.Counter(nums)
        # O(nlog(K))
        return heapq.nlargest(k, counts.keys(), key=counts.get)
