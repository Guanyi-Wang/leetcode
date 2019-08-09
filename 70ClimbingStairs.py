class Solution:
    # recursive solution O(2**n)
    def climbStairs(self, n: int) -> int:
        # climb from 0 to n
        return self.climb(0, n)

    def climb(self, i: int, n: int):
        '''
        i: start stair
        n: end stair
        '''
        if i > n:
            return 0
        if i == n:
            return 1
        # two ways to stair n using one step, either from one stair below or two stairs
        return self.climb(i+1, n) + self.climb(i+2, n)
#################################################

## Top down using memory list
class Solution:
    def climbStairs(self, n: int) -> int:
        # list to store memeory
        mem = [None] * (n + 1)
        mem[0] = 1
        mem[1] = 2
        return self.climb(n - 1, mem)

    def climb(self, n: int, mem: list) -> int:
        res = 0
        if mem[n] != None:
            return mem[n]
        else:
            res = self.climb(n - 1, mem) + self.climb(n - 2, mem)
        mem[n] = res
        return res
###################################################

## Bottom up
class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        pre1 = 2
        pre2 = 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n + 1):
            res = pre1 + pre2
            pre2 = pre1
            pre1 = res
        return res



