class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        count_L = count_R = 0
        for i in range(len(s)):
            if s[i]=='L':
                count_L += 1
            else:
                count_R += 1
            if count_L ==count_R and count_L != 0:
                count+=1
                count_L = count_R = 0
        return count