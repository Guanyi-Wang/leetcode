"""
Bitwise solution based on 43 = 3*2^3 + 3*2^2+ 3*2^0 +1.
43/3 = 2^3 +2^2+2^0
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if (dividend > 0) == (divisor > 0):
            sign = 1
        else:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        i = 31
        while i >= 0:
            if divisor > dividend:
                break
            if divisor << i <= dividend:
                res += 1<<i
                dividend -= divisor<<i
            i -= 1
        return res * sign