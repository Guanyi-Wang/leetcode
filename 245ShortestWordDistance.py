"""
Question
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example: Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:

You may assume word1 and word2 are both in the list.
"""
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            p = None
            sh_d = len(words)
            for i in range(len(words)):
                if words[i] == word1:
                    if p:
                        sh_d = min(sh_d, i-p)
                    p = i
        else:
            pw1 = pw2 = None
            sh_d = len(words)
            for i in range(len(words)):
                if words[i] == word1:
                    pw1 = i
                    if not pw2:
                        sh_d = min(sh_d, i - pw2)
                elif words[i] == word2:
                    pw2 = i
                    if not pw1:
                        sh_d = min(sh_d, i - pw1)
        return sh_d