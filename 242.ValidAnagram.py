from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # hash tabel to store characters and their appearances
        dic = {}
        for i in s:
            if i not in dic:
                # First apparence
                dic[i] = 1
            else:
                dic[i] += 1
        for j in t:
            if j in dic:
                dic[j] -= 1
                if dic[j] <0:
                    return False
            else:
                return False
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
