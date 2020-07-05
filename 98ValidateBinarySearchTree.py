# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.iVBST(root, None, None)
    def iVBST(self, node, min, max):
        if not node:
            return True
        if  min!=None and node.val <= min:
            return False
        if max!=None and node.val >= max:
            return False
        # The left subtree of a node contains only nodes with keys less than the node's key.
        # The right subtree of a node contains only nodes with keys greater than the node's key.
        return self.iVBST(node.left, min, node.val) and self.iVBST(node.right, node.val, max)