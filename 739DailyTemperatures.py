"""
Monotonic Stack
"""


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [None] * len(T)
        for i in range(len(T) - 1, -1, -1):  # put in in reversed order to pop in right order
            r = 1
            while stack and stack[-1][0] <= T[i]:
                stack.pop()
                r += 1
            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1][1] - i
            stack.append((T[i], i))
        return res
