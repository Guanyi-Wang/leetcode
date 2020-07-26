"""
https://leetcode.com/problems/bulls-and-cows/discuss/74616/3-lines-in-Python
comments from @lee215
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if not secret:
            return '0A0B'
        A = sum([a==b for a, b in zip(secret, guess)])
        # So elegent to use & to intersect dicts, see https://docs.python.org/3/library/collections.html#collections.Counter
        B = collections.Counter(secret) & collections.Counter(guess)
        return '{}A{}B'.format(A, sum(B.values())-A)