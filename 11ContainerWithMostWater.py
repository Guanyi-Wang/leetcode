from typing import List

"""
Run out of time method. Brute Force. O(N**2)
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for left in range(len(height) - 1):
            for right in range(len(height) - 1, left, -1):
                area = min(height[left], height[right]) * (right - left)
                res = max(area, res)
        return res


"""
Brute Force with modification. Trace the minimum height. Still O(N**2) but better.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        min_height = 0
        for left in range(len(height) - 1):
            if height[left] > min_height:
                for right in range(len(height) - 1, left, -1):
                    if height[right] > min_height:
                        min_height = min(height[left], height[right])
                        area = min_height * (right - left)
                        res = max(area, res)
        return res


"""
One iteration. 
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
