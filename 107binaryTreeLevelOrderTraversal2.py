# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        # A list to store all nodes in each level
        level = [root]
        while level:
            res.append([le.val for le in level])
            # A list to store nodes in the same level
            nodes = []
            for node in level:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            level = nodes
        return res[::-1]

