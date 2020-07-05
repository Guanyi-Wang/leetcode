"""
Use Fast Slow Pointers to find loop in the built function based on nums.
f(n) = nums[n](slow)     f(n) = nums[nums[n]] (fast)since each integer is between 1 and n
There will be loop since dupulicated n in nums
Step 1:
find intersection in the loop where fast = slow
step 2:
reset the slow from beginning and fast as same pace as slow from intersection. The next meeting point is start of loop which is duplicate.
Proof:
https://leetcode.com/articles/find-the-duplicate-number/
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t = h = nums[0]
        # step 1
        while True:
            t = nums[t] # slow
            h = nums[nums[h]] # fast twice of slow
            if t == h:
                break
        t = nums[0]
        while t !=h:
            t = nums[t]
            h = nums[h]
        return t