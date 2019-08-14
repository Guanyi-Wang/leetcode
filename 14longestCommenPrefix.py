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
print(longestCommonPrefix(["aa","a"]))