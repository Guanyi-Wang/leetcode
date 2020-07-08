"""
Copy nums and put it in the end: [1,2,1] ->[1,2,1,1,2,1]
Instead of doing real copy, iterate nums twice.
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        stack = []
        res = [None]*len(nums)
        for i in range(len(nums)*2, -1, -1): # double the index
            while stack and stack[-1] <= nums[i%len(nums)]:
                stack.pop()
            if not stack:
                res[i%len(nums)] = -1
            else:
                res[i%len(nums)] = stack[-1]
            stack.append(nums[i%len(nums)])
        return res[:len(nums)]