# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.min_index = 0
        self.sorted = self.sort(root)

    def sort(self, root):
        res = []
        if root:
            res.extend(self.sort(root.left))
            res.append(root.val)
            res.extend(self.sort(root.right))
        return res

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.sorted[self.min_index]
        self.min_index += 1
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.min_index < len(self.sorted)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()