"""
Use recursion. Two kinds of solutions for each case: either take this coin or skip this coin and go on.
Base case:
remain == 0, find one solution
remain < 0, wrong solution, already exceeded
i == len(coins), reach the last coin

"""
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.changeRecursion(amount, 0, coins)

    def changeRecursion(self, remain, i, coins):
        if remain == 0:
            return 1
        if remain < 0 or i == len(coins):
            return 0
        # either choose this coins or skip
        return self.changeRecursion(remain - coins[i], i, coins) + self.changeRecursion(remain, i + 1, coins)