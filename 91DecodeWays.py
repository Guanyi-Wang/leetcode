"""
DP
233222323 = 23322232|3 +2332223|23()
solution('233222323') =  solution('23322232') + solution('2332223')
solution [i] = sol[i-1] + sol[i+1] if 0<sol[i]<=9 and 10<=sol[i]<=26

"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp = [0 for x in range(len(s) + 1)] # '000'
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]