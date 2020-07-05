# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val == key:
            # find node
            # node has no leaf
            if not root.left and not root.right:
                return None
            # node has one leaf, return it
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # node has two leaf
            if root.left and root.right:
                # find the min(leftest) in right sub-tree (or max in left)
                node = root.right
                while node.left:
                    node = node.left
                root.val = node.val
                # delete node in its right sub_tree
                root.right = self.deleteNode(root.right, root.val)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root