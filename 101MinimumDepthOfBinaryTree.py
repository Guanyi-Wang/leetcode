# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = [root]
        depth = 0
        while level:
            nodes = []
            depth += 1
            for node in level:
                if not node:
                    continue
                if node.left == None and node.right == None:
                    return depth
                nodes.append(node.left)
                nodes.append(node.right)
            level = nodes
