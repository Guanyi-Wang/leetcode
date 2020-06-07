"""
x^n = x^(n//2)*x^(n//2)*x if n is odd
x^n = x^(n//2)*x^(n//2)   if n is even
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        def powRecursion(x:float, n:int) -> float:
            if n == 1:
                return x
            if n & 1 ==1:  # n is odd
                re = powRecursion(x, n//2)
                return re*re*x
            else:
                re = powRecursion(x, n//2)
                return re*re
        if n < 0:
            return 1/powRecursion(x, abs(n))
        else:
            return powRecursion(x, n)