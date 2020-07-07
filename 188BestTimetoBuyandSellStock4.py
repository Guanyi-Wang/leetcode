"""
DP
dp_i_hold_k  k: k transactions happened, k-1 when you buy(sell is the same)
dp[i][0][k] = max(dp[i-1][0][k], dp[i-1][1][k] + prices[i])
dp[i][1][k] = max(dp[i-1][1][k], dp[i-1][0][k-1] - prices[i])
base cases:
k == 0
dp_i_0_0 = 0 # unhold the stock
dp_i_1_0 = float('-inf') # hold the stock but no transactions, impossible
i == 0
dp_0_1_k = -prices[0] # buy the first day
dp_0_0_k = 0 # didn't buy the first
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if k>=n/2: # same as k == infinite
            dp_i_0 = 0
            dp_i_1 = float('-inf')
            for i in range(len(prices)):
                dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
                dp_i_1 = max(dp_i_0-prices[i], dp_i_1)
            return dp_i_0
        dp_0 = [[None]*(k+1)for i in range(len(prices))]
        dp_1 = [[None]*(k+1)for i in range(len(prices))]
        for i in range(len(prices)):
            for j in range(k+1):
                if i==0: # base case
                    dp_0[0][j] = 0
                    dp_1[0][j] = -prices[0]
                elif j==0: # base case
                    dp_0[i][0] = 0
                    dp_1[i][0] = float('-inf')
                else:
                    dp_1[i][j] = max(dp_1[i-1][j], dp_0[i-1][j-1] - prices[i])
                    dp_0[i][j] = max(dp_0[i-1][j], dp_1[i-1][j] + prices[i])
        return dp_0[n-1][k]

