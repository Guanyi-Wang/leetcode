# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preoder(root, res)
        return res
    def preoder(self, node, res):
        if not node:
            return
        res.append(node.val)
        self.preoder(node.left,res)
        self.preoder(node.right,res)


# iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = collections.deque([root])
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res