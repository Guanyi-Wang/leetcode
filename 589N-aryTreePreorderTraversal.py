"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# recursive
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = [root.val]
        for n in root.children:
            res.extend(self.preorder(n))
        return res
# iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = collections.deque([root])
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(reversed(node.children))
        return res