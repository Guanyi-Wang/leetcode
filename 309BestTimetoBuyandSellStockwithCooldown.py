class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp0 = [None]*(len(prices)+1)
        dp1 = [None]*(len(prices)+1)
        # base cases
        dp0[0] = 0
        dp0[1] = 0
        dp1[0] = float('-inf')
        dp1[1] = -prices[0]
        for i in range(2,len(prices)+1):
            print(i)
            dp0[i] = max(dp0[i-1], dp1[i-1]+prices[i-1])
            dp1[i] = max(dp0[i-2]-prices[i-1], dp1[i-1])
        return dp0[-1]