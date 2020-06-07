from typing import List
import collections
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return 0
        l = r = 0
        dic = collections.Counter()
        max_len = 0
        for r in range(len(tree)):
            dic[tree[r]] += 1
            # remove left first fruit one by one until only one type left
            while len(dic)>2:  # more than 2 types of fruit
                dic[tree[l]] -= 1
                if dic[tree[l]] == 0: # remove empty entry
                    del dic[tree[l]]
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len

    class Solution:
        def totalFruit(self, tree: List[int]) -> int:
            if not tree:
                return 0
            l = r = 0
            dic = collections.Counter()
            max_len = 0
            for r in range(len(tree)):
                dic[tree[r]] += 1
                # remove left first fruit one by one until only one type left
                while len(dic) > 2:  # more than 2 types of fruit
                    dic[tree[l]] -= 1
                    if dic[tree[l]] == 0:  # remove empty entry
                        del dic[tree[l]]
                    l += 1
                max_len = max(max_len, r - l + 1)
            return max_len
"""
Real O(N) solution, without shrinking the window
"""
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return 0
        l = r = 0
        dic = collections.Counter()
        for r in range(len(tree)):
            dic[tree[r]] += 1
            # remove left first fruit one by one until only one type left
            if len(dic) > 2:  # more than 2 types of fruit
                dic[tree[l]] -= 1
                if dic[tree[l]] == 0:  # remove empty entry
                    del dic[tree[l]]
                l += 1
        return r - l + 1