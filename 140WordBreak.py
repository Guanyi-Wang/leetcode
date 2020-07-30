class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        seen = collections.defaultdict(list)
        return self.dfs(s, seen, word_set)

    def dfs(self, s, seen, word_set):
        if s in seen:
            return seen[s]
        if not s:  # special case for empty string at the end
            return None
        res = []
        for i in range(len(s)):
            if s[:i + 1] in word_set:
                rem = self.dfs(s[i + 1:], seen, word_set)
                if not rem and i + 1 == len(s):  # make sure it's the last empty string instead of not matched string
                    res.append(s[:i + 1])
                else:  # add first part with all possible last part
                    for r in rem:
                        res.append(s[:i + 1] + ' ' + r)
        seen[s] = res
        return res
