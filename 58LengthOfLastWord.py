class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or s==' ':
            return 0
        # Find the first non-empty character in reversed order
        for i in range(len(s)-1,-2,-1):
            if s[i] != ' ' or i == -1:  # If i == -1 means all blank character
                break
        # Find the firt empty character from i to -1
        for j in range(i,-2,-1):
            if s[j]==' ' or j == -1: # j == -1 means word starts from beginning
                return i - j
            