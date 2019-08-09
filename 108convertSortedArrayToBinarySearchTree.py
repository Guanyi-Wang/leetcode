# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        def bst(start:int, end:int, nums: List[int]):
            if start>end:
                return None
            mid = (start + end)//2
            # find the middle value as the root node in each steps
            root = TreeNode(nums[mid])
            # add left subtree and right subtree recursively
            root.left = bst(start, mid-1, nums)
            root.right = bst(mid+1, end, nums)
            return root
        return bst(0, len(nums)-1, nums)