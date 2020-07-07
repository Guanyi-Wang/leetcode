# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dp(root):
            """
            return list of two: max of rob this node and max of not rob this node
            [not_rob, rob ]
            """
            if not root:
                return [0, 0]
            left = dp(root.left)
            right = dp(root.right)
            # rob this node, children is safe
            rob = root.val + left[0] + right[0]
            # not rob this node, children can be robbed or not depends on profit
            not_rob = max(left[0], left[1]) + max(right[0], right[1])
            return [not_rob, rob]

        return max(dp(root))
