"""
BackTrack DFS
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        self.findPath(root, [root], path, p, q)
        # print(path)
        i = 0
        while path[0][i] == path[1][i]:
            if i == min(len(path[0]), len(path[1])) - 1:
                return path[0][i]
            i += 1
        return path[0][i - 1]

    def findPath(self, node, temp, path, p, q):
        if node == p or node == q:
            path.append(temp)
        if not node:
            return False
        self.findPath(node.left, temp + [node.left], path, p, q)
        self.findPath(node.right, temp + [node.right], path, p, q)


"""
Use BST's characteristics.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root