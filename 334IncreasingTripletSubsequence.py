class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n<=first: # always keep the smallest
                first = n
            elif n<= second: # first<n<second
                second = n
            else: # n>second>first
                return True
        return False