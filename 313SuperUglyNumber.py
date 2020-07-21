"""
Heap Solution
take [2,3,5] as primes
res = [1] result starts from 1, multiply with [2, 3, 5] and put the results in a heap.
In each step, pop the min result in the heap as nth ugly number.
Use this ugly number to multiply with [2,3,5] again.
Use a dict to avoid duplicates.
O(NlogN)
"""
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        hp = [1]
        res = []
        seen = {}
        for i in range(n-1):
            min_p = heapq.heappop(hp)
            for p in primes:
                product = min_p * p
                if product not in seen:
                    seen[product] = 1
                    heapq.heappush(hp, product)
        return heapq.heappop(hp)