# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        dq = collections.deque([])
        res = []
        node = root
        while dq or node:
            if node:
                dq.append(node)
                node = node.left
            else:
                node = dq.pop()
                res.append(node.val)
                node = node.right
        return res


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.reTraversal(root, res)
        return res

    def reTraversal(self, cur, res):
        if not cur:
            return
        self.reTraversal(cur.left, res)
        res.append(cur.val)
        self.reTraversal(cur.right, res)


