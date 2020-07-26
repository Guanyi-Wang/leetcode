
"""
Try to sperate two distinct num into two partitions along with other duplicate nums.
Like we did in Single Number1, XOR all numbers to get the XOR result of two distinct nums.
Use the previous XOR result and its low bit (set bit) to partition nums into two, one will contain each distinct num.
eg:
[1,2,1,3,2,5] --> b[001, 010, 001, 011, 010, 101]
XOR all num in nums:
num appear twice will be 000, so result will be 3 XOR 5: 110
110 means the second digit and third digit of 3(011) and 5(101) is different.
Here we use the difference in the second digit(first digit with 1 so called low set bit):
formula to get low bit: low_bit = x&(-x)  or x&(~x-1)
use 10 to AND all num in nums:
    if num & 10:
        num will be put into partition1(second digit is 1 like 3)
    else:
        num will be put into partition2(second digit is 0 like 5)
so we sperated 3 and 5 into different partitions, each partition has some dupulicated num apparing twice.
Use trick in Single Number 1 to XOR all nums in each partition and we get two distinct nums.

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        # first round XOR to get XOR of two distinct nums
        xor = reduce(lambda x,y: x^y, nums)
        # get the low set bit using formula: x&(-x)
        low_bit = xor&(-xor)
        p1 = p2 = 0
        for num in nums:
            if num & low_bit:
                p1^=num
            else:
                p2^=num
        return[p1, p2]