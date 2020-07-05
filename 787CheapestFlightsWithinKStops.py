"""
Dijkstra's Algorithm
"""
from typing import List
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adjac_dic = collections.defaultdict(list)
        for s, d, p in flights:
            adjac_dic[s].append((d, p))  # build adjancent matrix
        priority_queue = [(0, -1, src)]  # (cost, node, steps)
        while priority_queue:
            cost, step, node = heapq.heappop(priority_queue)  # pop the one with lowest cost
            if step > K:
                continue  # stop relaxing this routine
            if node == dst:
                return cost
            for d, p in adjac_dic[node]:  # add all adjacent nodes
                heapq.heappush(priority_queue, (p + cost, step + 1, d))

        return -1