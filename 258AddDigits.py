"""
pattern
0->0
1~9->1~9
10~18->1~9
19~27->1~9
(num-1)%9+1
"""
class Solution:
    def addDigits(self, num: int) -> int:
        if num<=0:
            return 0
        return (num-1)%9+1