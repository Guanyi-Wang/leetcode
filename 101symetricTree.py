# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## recursive method
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, tree1: TreeNode, tree2: TreeNode):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        if tree1.val != tree2.val:
            return False
        else:
            return self.isMirror(tree1.left, tree2.right) and self.isMirror(tree1.right, tree2.left)

###############################
## iterative method
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [(root, root)]
        while queue:
            tree1, tree2 = queue.pop(0)
            if not tree1 and not tree2:
                continue
            elif not tree1 or not tree2:
                return False
            elif tree1.val != tree2.val:
                return False
            else:
                queue.append((tree1.left, tree2.right))
                queue.append((tree1.right, tree2.left))
        return True