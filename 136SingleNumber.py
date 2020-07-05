"""
a XOR a = 0
a XOR a XOR b XOR c XOR c = b XOR 0 = b
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x^y, nums)