"""
DP
dp_i_hold_k  k: k transactions happened, k-1 when you buy(sell is the same)
dp[i][0][k] = max(dp[i-1][0][k], dp[i-1][1][k] + prices[i])
dp[i][1][k] = max(dp[i-1][1][k], dp[i-1][0][k-1] - prices[i])
k = 2 enumerate base cases"
dp_i_0_1 = float('-inf')
dp_i_0_2 = 0
dp_i_1_1 = float('-inf')
dp_i_1_2 = float('-inf')
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # base case (dp_i_hold_k)
        dp_i_0_0 = 0
        dp_i_0_1 = 0
        dp_i_0_2 = 0
        dp_i_1_1 = float('-inf')
        dp_i_1_2 = float('-inf')
        for i in range(len(prices)):
            dp_i_1_2 = max(dp_i_1_2, dp_i_0_1 - prices[i])
            dp_i_0_1 = max(dp_i_0_1, dp_i_1_1 + prices[i])
            dp_i_0_2 = max(dp_i_0_2, dp_i_1_2 + prices[i])
            dp_i_1_1 = max(dp_i_1_1, dp_i_0_0 - prices[i])
        return dp_i_0_2

