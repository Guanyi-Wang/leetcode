"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        queue = collections.deque([])
        if root:
            queue.append(root)
            while queue:
                temp = []
                for i in range(len(queue)):
                    node = queue.popleft()
                    temp.append(node.val)
                    queue.extend(node.children or [])
                res.append(temp)
        return res

