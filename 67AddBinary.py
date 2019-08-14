class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, value, result = 0, 0, ''
        # Choose the longer length as iterator:
        for i in range(max(len(a), len(b))):
            # Reset value to carry
            value = carry
            if i < len(a):
                value += int(a[-i - 1])
            if i < len(b):
                value += int(b[-i - 1])
            value, carry = value % 2, value // 2
            result += str(value)
        if carry == 1:
            result += '1'
        return str(result[::-1])

