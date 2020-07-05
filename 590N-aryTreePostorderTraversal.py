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

# recursive
# iterative
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return[]
        res = []
        for node in root.children:
            res.extend(self.postorder(node))
        res.append(root.val)
        return res