# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            res.extend(self.postorderTraversal(root.left))
            res.extend(self.postorderTraversal(root.right))
            res.append(root.val)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = collections.deque([])
        res = []
        stack.append([root, False]) # flag to indicate 1st or 2nd time visited
        while stack:
            node, flag = stack.pop()
            if node:
                if flag:
                    res.append(node.val)
                else:
                    stack.append([node, True])
                    stack.append([node.right, False])
                    stack.append([node.left, False])
        return res