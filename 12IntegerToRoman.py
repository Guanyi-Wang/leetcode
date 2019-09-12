class Solution:
    def intToRoman(self, num: int) -> str:
        rom = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
               5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        while num != 0:
            for r in rom:
                if num >= r:
                    num -= r
                    res += rom[r]
                    ## start another iteration from the largest possible
                    break
        return res
