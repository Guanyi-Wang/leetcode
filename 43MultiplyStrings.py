"""
Use distributive Law: 123*45 = (100+20+3)*(40+5)
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == '0' or num2[0] == '0':
            return '0'
        res = 0
        for i, d1 in enumerate(num1[::-1]):
            d1 = ord(d1) - ord('0')
            for j, d2 in enumerate(num2[::-1]):
                d2 = ord(d2) - ord('0')
                product = d1 * 10 ** i * d2 * 10 ** j
                res += product
        return str(res)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == '0' or num2[0] == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))  # zero padding
        loc = len(res) - 1  # start from last digit
        for n1 in num1[::-1]:
            tem_loc = loc
            for n2 in num2[::-1]:
                product = (ord(n1) - ord('0')) * (ord(n2) - ord('0'))
                res[tem_loc] += product  # add carry on this digit
                res[tem_loc - 1] += res[tem_loc] // 10  # log carry on higher digit
                res[tem_loc] = res[tem_loc] % 10  # update this digit
                tem_loc -= 1
            loc -= 1
        #  remove zero padding
        p = 0
        while p < len(res) - 1 and res[p] == 0:
            p += 1
        return ''.join(map(str, res[p:]))
