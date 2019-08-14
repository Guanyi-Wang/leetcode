# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        # A function to find the max depth in a tree
        def maxDepth(root: TreeNode):
            if not root:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        # heights of left subtree and right subtree differs more than one
        if abs(maxDepth(root.left) - maxDepth(root.right)) > 1:
            return False
        # check all the subtrees
        return self.isBalanced(root.left) and self.isBalanced(root.right)
###############################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if self.getHeight(root) == -1:
            return False
        return True

    def getHeight(self, root: TreeNode):
        if not root:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight == -1 or rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1

