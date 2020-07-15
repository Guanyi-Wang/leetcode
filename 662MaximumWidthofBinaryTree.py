"""
BFS
store(node, count) in queue
node.left -> (node.left, 2*count-1)
node.right -> (node.right, 2*count)
find left most and right most in each level and get max difference
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        counts = []
        while queue:
            left = right = 0
            size = len(queue)
            for i in range(size):
                node, count = queue.popleft()
                if i == 0:
                    left = count
                if i == size-1:
                    right = count
                if node.left:
                    queue.append((node.left, count*2-1))
                if node.right:
                    queue.append((node.right, count*2))
            # print(left, right)
            counts.append(right-left+1)
            # print(counts)
        return max(counts)