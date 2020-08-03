class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s:
            return True
        dict = {}
        mapped = set()
        for i in range(len(s)):
            if s[i] in dict:
                if dict[s[i]]!= t[i]:
                    return False
            elif t[i] in mapped:
                return False
            else:
                dict[s[i]] =t[i]
                mapped.add(t[i])
        return True