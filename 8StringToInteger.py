class Solution:
    def myAtoi(self, str: str) -> int:
        res = ''
        # remove white space
        str = str.strip()
        # empty string
        if not str:
            return 0
        # first digit
        if not str[0].isdigit() and not str[0] in ['-', '+']:
            return 0
        # extract the sign of digit
        if str[0] == '-':
            sign = -1
        else:
            sign = 1
        # extract the first digit sequence
        if not str[0] in ['-','+']:
            for s in str:
                if s.isdigit():
                    res += s
                else: break
        else:
            for s in str[1:]:
                if s.isdigit():
                    res +=s
                else: break
        # no digit
        if not res:
            return 0
        # overflow
        if int(res)*sign > 2 ** 31 -1:
            return 2**31 -1
        if int(res)*sign < -2**31:
            return -2**31
        return int(res)*sign