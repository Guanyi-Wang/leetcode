"""
DP
state expression: dp[i][hold or not]
dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]) no hold = max(nohold, hold+sell)
dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]) hold = max(hold, nohold-buy)

base case:

dp[0][0]: 0
dp[0][1]: -inf (impossible situation)
only need previous state to calculate next state. Space optimization
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_0-prices[i], dp_i_1)
        return dp_i_0