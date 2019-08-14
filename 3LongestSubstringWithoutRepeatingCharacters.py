class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = {}
        max_len = 0
        max_str = ''
        for i in range(len(s)):
            temp[s[i]] = i
            j = i+1
            while j<len(s) and s[j] not in temp:
                temp[s[j]] = j
                j = j+1
            if max_len< len(temp):
                max_len = len(temp)
                max_str = str(temp)
            temp = {}
        return max_len

##################################
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = {}
        max_len = 0
        i = 0
        for j in range(len(s)):
            if s[j] in temp:
                max_len = max(j - i - 1, max_len)
                i = temp.get(s[j])
                temp.clear()
            temp[s[j]] = j
            j = j + 1
        max_len = max(j - i, max_len)
        return max_len

