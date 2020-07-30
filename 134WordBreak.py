"""
DFS with memory.
dfs[i] = word1+dfs[word1:] or word2+dfs[word2:] or ...

"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        seen = {}

        def dfs(start):
            if start in seen:
                return seen[start]
            if start == len(s):
                return True
            for word in word_set:
                if len(word) <= len(s) - start and s[start:start + len(word)] in word_set and dfs(start + len(word)):
                    seen[start] = True
                    return True
            seen[start] = False
            return False

        return dfs(0)


"""
BFS with memory.
But still TLE
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        seen = collections.defaultdict(list)
        queue = collections.deque([0])
        while queue:
            start = queue.popleft()
            if start in seen:
                queue.extend(seen[start])
            if start == len(s):
                return True
            for end in range(start, len(s)):
                if s[start:end + 1] in word_set:
                    seen[start].append(end + 1)
                    queue.append(end + 1)
        return False
"""
DP
dp = [T, F, F, T, F, F, T]
s =  [  'c  a  t  d  o  g']
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for word in wordDict:
                    if s[i:i+len(word)]==word:
                        dp[i+len(word)] = True
        return dp[-1]