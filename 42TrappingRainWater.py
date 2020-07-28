"""
trapped_water[i] = min(highest_left, highest_right)-height[i]
O(n^2)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(1, len(height)-1):
            r = min(max(height[:i]), max(height[i+1:])) -height[i]
            if r >0:
                res+=r
        return res
"""
Two pointers to optimize process to find highest_left and highes_right
trapped_water[i] = min(highest_left, highest_right)-height[i]
left = 0, right =len(height)-1
h_left = height[left], h_right = height[right], representing the highest left of height[left] and right
move left or right till they meet, since water is only influnced by min(h_l, h_r), we calculate shorter part
and move it to the mid.
O(N)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        res = 0
        left = 0
        right =len(height)-1
        h_left = height[left]
        h_right = height[right]
        while left<right:
            # update hightest left and right
            h_right = max(h_right, height[right])
            h_left = max(h_left, height[left])
            if h_left<=h_right:
                res+= h_left - height[left]
                left += 1
            else:
                res += h_right - height[right]
                right -= 1
        return res