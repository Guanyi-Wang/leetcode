"""
BFS solution. push leafs node of one layer, count +1. return the count when meet the first no leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        dq = collections.deque([root])
        while len(dq):
            size = len(dq)
            for i in range(size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                if not node.left and not node.right:
                    return res
            res += 1
        return res