import collections

# slicing window O(N), O(N)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        if k >= len(s):
            return len(s)
        longest_len = 0
        l = r = 0  # left and right pointers start from beginning, representing a sliding window
        change_counter = 0  # number of characters need to be changed in the window
        char_dic = collections.Counter()  # unique character as key in the current window, with its count as value
        for r in range(len(s)):
            char_dic[s[r]] += 1  # increase its count in memory
            most_common_count = char_dic.most_common(1)[0][1]
            change_counter = r - l + 1 - most_common_count  # change all the other ones
            if change_counter > k:  # more changes needed than k
                char_dic[s[l]] -= 1  # reduce its count in current window
                l += 1  # move left pointer
            longest_len = max(longest_len, r - l + 1)
        return longest_len
