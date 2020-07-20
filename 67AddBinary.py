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

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return a+b
        res = []
        len_a = len(a)-1
        len_b = len(b)-1
        carry = 0
        while len_a>=0 or len_b>=0 or carry:
            s = (len_a >=0 and a[len_a]=='1') + (len_b >=0 and b[len_b]=='1') + carry
            res.append(str(s%2))
            carry = 1 if s>=2 else 0
            len_a -= 1
            len_b -= 1
        return '1'+''.join(res[::-1]) if carry ==1 else ''.join(res[::-1])