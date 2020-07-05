"""
DP
dp[0] = 0
dp[1] = dp[0]+1 = 1
dp[2] = dp[1]+1 = 2
dp[3] = dp[2]+1 = 3
dp[4] = Min{ dp[4-1*1]+1, dp[4-2*2]+1 }
      = Min{ dp[3]+1, dp[0]+1 }
      = 1
dp[5] = Min{ dp[5-1*1]+1, dp[5-2*2]+1 }
      = Min{ dp[4]+1, dp[1]+1 }
      = 2
While j*j <=n
dp[n] = min(dp[n-j*j]+1)
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            j = 1
            m = dp[i]
            while j * j <= i:
                m = min(dp[i - j * j] + 1, m)
                j += 1
            dp[i] = m
        return dp[n]


"""
BFS 
for example 10, [1,2*2,3*3]
                   10
            /       |     \
          10-1    10-4   10-9
        /  |  \     |  \   |
       8   5   0
"""


class Solution:
    def numSquares(self, n: int) -> int:
        # list of perfect squares less than n
        ps = [i * i for i in range(1, n + 1) if i * i <= n]
        queue = collections.deque([(n, 0)])
        while queue:
            for i in range(len(queue)):
                remain, count = queue.popleft()
                for s in ps:
                    if s == remain:
                        return count + 1
                    if s < remain:
                        queue.append((remain - s, count + 1))
                    else:
                        break


