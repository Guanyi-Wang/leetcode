class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        return c.most_common()[-1][0]

"""
Bit manipulate
eg:
[010,010,011,010]  (2,2,3,2)
first bit: (0+0+0+1)%3 = 1
second bit: (1+1+1+1)%3 = 1
third bit: (0+0+0+0) = 0
result: 011->3 
for negative numbers:
python use complement of -x-1 as binary format:
eg: b(-10) = b(~9)
so b(-10) = 1111....110110
-10 = (1*2^30+..+1*2^5+1*2^4+0*2^3+1*2^2+1*2^1+0*2^0)- 1*2^31
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        res = 0
        for i in range(32):
            sum = 0
            for num in nums:
                sum += num>>i&1
            rem = sum%3
            if i == 31 and rem: # 1 in 31 digit means negative
                res -=rem<<i
            else:
                res |= rem<<i
        return res
"""
https://leetcode.com/problems/single-number-ii/discuss/43412/Python-Bit-Manipulation-(with-more-general-case)
eg:[010, 010, 011, 010]
x = 010: 
one = 000 xor 010 = 010
two = 000 or (010 and 010) = 010
three = 010 and 010 = 010
one = 010 and reverse(010) = 000
two = 010 and reverse(010) = 010
x = 010:
one = 000 xor 010 = 010
two = 010 or (010 and 010) = 010
three = 010 and 010 = 010
one = 010 and reverse(010) = 000
two = 010 and reverse(010) = 010
x = 011
one = 010 xor 011 = 001
two = 010 or (001 and 011) = 000
three = 
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for x in nums:
            one, two, three = one ^ x, two | (one & x), two & x
            one, two = one & ~three, two & ~three
        return one