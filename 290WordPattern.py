class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = str.split(' ')
        dict = {}
        mapped = set()
        if len(s)!= len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dict:
                if dict[pattern[i]] != s[i]:
                    return False
            elif s[i] in mapped:
                return False
            else:
                dict[pattern[i]] = s[i]
                mapped.add(s[i])
        return True