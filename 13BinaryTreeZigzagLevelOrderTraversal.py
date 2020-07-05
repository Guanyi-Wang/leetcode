# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque([])
        queue.append(root)
        res = []
        count = 0
        if not root:
            return res
        while queue:
            temp = []
            count += 1
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not count%2:
                res.append(reversed(temp))
            else:
                res.append(temp)
        return res