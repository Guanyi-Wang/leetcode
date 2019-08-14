# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
###################################################################3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # list store all nodes in each level
        level = [root]
        depth = 0
        while level:
            # list to store nodes in the same level in each iteration
            nodes = []
            depth += 1
            for node in level:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            level = nodes
        return depth
##############################################################
