class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        left, right = 0, x
        while left <= right:
            mid = int((left+right)/2)
            if mid**2<=x and (mid+1)**2 >x:
                return mid
            elif mid**2 < x:
                left = mid
            else: right = mid