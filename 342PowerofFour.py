class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if not num:
            return False
        while num !=1:
            if num%4:
                return False
            num = num / 4
        return True


"""
Follow up:
power of 4
1
100
10000
1000000
100000000
10000000000
...
start with one and followed by even number of 0s
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        s = bin(num)[3:]
        return '1' not in s and len(s) % 2 == 0
