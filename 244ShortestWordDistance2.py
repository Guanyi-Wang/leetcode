"""
Question
Design a class which receives a list of words in the constructor, and implements
a method that takes two words word1 and word2 and return the shortest distance between
these two words in the list. Your method will be called repeatedly many times with different
 parameters.

Example:

Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:

You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
import collections
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.word_dict = collections.defaultdict(list)
        self.len = len(words)
        for i, word in enumerate(words):
            self.word_dict[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pw1 = pw2 = 0
        sh_d = self.len
        i1 = self.word_dict[word1]
        i2 = self.word_dict[word2]
        while True:
            w1 = i1[pw1]
            w2 = i2[pw2]
            sh_d = min(sh_d, abs(w1-w2))
            if w1<w2:
                pw1+=1
            else:
                pw2+=1
            if pw1 > len(i1)-1 or pw2>len(i2)-1:
                return sh_d


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)