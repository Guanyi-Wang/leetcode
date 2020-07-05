# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1


"""
Depth of tree == root to left most leaf.
Based on "all nodes in the last level are as far left as possible"
if depth of left tree== depth of right tree:
    left tree is perfect bst (num of node = 2**h -1)
    right tree is complete bst (of course)
if depth of left tree > depth of right tree:
    right tree is perfect bst (binary tree every level, except possibly the last, is completely filled)
    left tree is complete bst (of course)
"""


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d_left = self.depth(root.left)
        d_right = self.depth(root.right)
        if d_left == d_right:
            return 1 + 2 ** d_left - 1 + self.countNodes(root.right)
        if d_left > d_right:
            return self.countNodes(root.left) + 1 + 2 ** d_right - 1

    def depth(self, node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d