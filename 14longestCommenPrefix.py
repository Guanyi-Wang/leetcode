def longestCommonPrefix(strs: [str]) -> str:
    res = ''
    if strs == []:
        return ''
    for i in range(len(strs[0])):
        for s in strs[1:]:
            if i+1 > len(s) :
                return res
            if s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for s in strs:
                if shortest[i]!=s[i]:
                    return shortest[:i]
        return shortest