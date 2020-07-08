class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return
        if not nums2:
            return [-1]*len(nums1)
        stack = []
        dic = {}
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if not stack:
                dic[nums2[i]] = -1
            else:
                dic[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        res = []
        for i in range(len(nums1)):
            if nums1[i] in dic:
                res.append(dic[nums1[i]])
            else:
                res.append(-1)
        return res