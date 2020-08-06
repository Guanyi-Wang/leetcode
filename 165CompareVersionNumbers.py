class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        s1 = sum([int(s)*(10**(-i)) for i, s in enumerate(v1)])
        s2 = sum([int(s)*(10**(-i)) for i, s in enumerate(v2)])
        if s1<s2:
            return -1
        if s1 > s2:
            return 1
        return 0