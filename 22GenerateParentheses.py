from typing import List

"""
Find all possible combinations and then eliminate illegal ones.
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = ['(']
        for i in range(2 * n - 1):
            temp = []
            for r in res:
                temp.append(r + '(')
                temp.append(r + ')')
            res = temp
        temp = []
        for r in res:
            if self.valid(r):
                temp.append(r)
        return temp

    def valid(self, s: str) -> bool:
        counter = 0
        for ch in s:
            if ch == '(':
                counter += 1
            else:
                counter -= 1
                if counter < 0:
                    return False
        if counter == 0:
            return True
        else:
            return False