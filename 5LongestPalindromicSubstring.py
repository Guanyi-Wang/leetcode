"""
Brute force method. Find all possible start and end and check if it is parlindrome.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # one character is a palindome as itself
        if not s or len(s) == 1:
            return s
        start, end = 0, 0
        # index of all possible starts
        for i in range(len(s) - 1):
            # index of all possible ends
            for j in range(i + 1, len(s)):
                # check if substring is a longer palindromic
                if s[i:j + 1] == s[i:j + 1][::-1] and j - i > end - start:
                    start, end = i, j
        return s[start: end + 1]


"""
Find the centre point and expand,  two cases considered: even('abba') or odd('aba')
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        # find all possible center point
        for i in range(len(s)):
            # if it's an odd substring
            odd = self.palindrom(s, i - 1, i + 1)
            if len(odd) > len(res):
                res = odd
            # if it's an even
            even = self.palindrom(s, i, i + 1)
            if len(even) > len(res):
                res = even
        return res

    def palindrom(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

