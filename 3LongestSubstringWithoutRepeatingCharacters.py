# Brute force O(n**2) O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        # iterate all start index
        max_len = 0
        for i in range(len(s)):
            dic = {}
            dic[s[i]] = i
            # iterate all end index
            for j in range(i+1, len(s)):
                if s[j] not in dic:
                    dic[s[j]] = j
                else:
                    break
            max_len = max(len(dic), max_len)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        max_len = 0
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            if s[j] in dic:
                max_len = max(max_len, len(dic))
                i = i+1
                j = i+1
                dic.clear()
                dic[s[i]] = i
            else:
                dic[s[j]] = j
                j = j+1
        max_len = max(max_len, len(dic))
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        dic = {}
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in dic:
                dic[s[j]] = j
                j += 1
            else:
                i = dic[s[j]] + 1
                j = i
                max_len = max(len(dic), max_len)
                dic.clear()
        max_len = max(len(dic), max_len)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = {}
        l = 0
        r = 0
        for r in range(len(s)):
            if s[r] not in seen:  # unseen character
                max_len = max(max_len, r - l + 1)
            elif l > seen[s[r]]:  # seen but not in the current window
                max_len = max(max_len, r - l + 1)
            else:  # seen in current window
                l = seen[s[r]] + 1  # new window start from right next of seen character
            seen[s[r]] = r  # need to update new location value in each iteration
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

