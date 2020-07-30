"""
Two pass and use a list to store candies.
"""


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        candies = [1] * len(ratings)
        # foward
        for i in range(1, len(candies)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        # backward
        for i in range(len(candies) - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                candies[i] = max(candies[i + 1] + 1, candies[i])
        return sum(candies)
