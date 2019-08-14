class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        rev = 0
        while x != 0:
            dig = int(x % 10)
            x = int(x / 10)
            rev = rev * 10 + dig
        if rev * flag < -2 ** 31 or rev * flag > 2 ** 31 - 1:
            return 0
        return rev * flag
