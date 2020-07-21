"""
 p2  p3  p5
[2, 3, 5]

        p5    p3    p2
 res = [1, 2, 3, 4, 5, 6,  ]

"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [None for i in range(n)]
        res[0] = 1
        p2 = p3 = p5 = 0
        for i in range(1, n):
            res[i] = min([res[p2] * 2, res[p3] * 3, res[p5] * 5])
            if res[i] == res[p2] * 2:
                p2 += 1
            if res[i] == res[p3] * 3:
                p3 += 1
            if res[i] == res[p5] * 5:
                p5 += 1
        return res[n - 1]