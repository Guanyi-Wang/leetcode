import collections
'''
Solution 1
Two string is permutation if and only if its distribution is same.
Use Counter to describe a subsequence's distribution.
O(N**2) O(26)
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2:
            return False
        # build hash map for chars in s1. {key: char, value: count}
        s1_dic = collections.Counter(s1)
        r = 0  # pointers
        for r in range(len(s2)-len(s1)+1):
            if s2[r] in s1_dic:
                s2_dic = collections.Counter(s2[r:len(s1)+r])  # Compare Distribution
                if s2_dic == s1_dic:
                    return True
        return False

'''
Solution 2
dont need to compare whole subsequence for each iteration. Update the s2_dic instead
O(N**2) O(26)
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2:
            return False
        # build hash map for chars in s1. {key: char, value: count}
        s1_dic = collections.Counter(s1)
        s2_dic = collections.Counter(s2[:len(s1)])
        # left and rght pointers
        l = 0
        r = len(s1)
        while r < len(s2):
            if s1_dic == s2_dic:
                return True
            else:
                s2_dic[s2[l]] -= 1 # left move forward, update count in dic
                if s2_dic[s2[l]] < 1:  # remove key with zero counts
                    s2_dic.pop(s2[l])
                s2_dic[s2[r]] = s2_dic.get(s2[r]) + 1  # update new char
                l += 1
                r += 1
        return s1_dic == s2_dic