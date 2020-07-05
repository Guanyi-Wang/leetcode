# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        nums = []
        self.dfs(root, nums, '')
        return sum(nums)

    def dfs(self, node, nums, temp):
        if node.left:
            self.dfs(node.left, nums, temp + str(node.val))
        if node.right:
            self.dfs(node.right, nums, temp + str(node.val))
        if not node.left and not node.right:
            nums.append(int(temp + str(node.val)))
