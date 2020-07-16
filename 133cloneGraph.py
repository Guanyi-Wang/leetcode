"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
BFS
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        queue = collections.deque([node])
        c_node = Node(node.val, [])
        seen = {node: c_node}  # dict to store node and copied node
        while queue:
            n = queue.popleft()
            for i in range(len(n.neighbors)):
                if n.neighbors[i] not in seen:
                    c_neig = Node(n.neighbors[i].val)
                    seen[n.neighbors[i]] = c_neig
                    seen[n].neighbors.append(c_neig)
                    queue.append(n.neighbors[i])
                else:
                    seen[n].neighbors.append(seen[n.neighbors[i]])
        return c_node
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
DFS
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        stack = [node]
        c_node = Node(node.val, [])
        seen = {node: c_node}
        while stack:
            n = stack.pop()
            for nei in n.neighbors:
                if nei not in seen:
                    c_nei  = Node(nei.val, [])
                    seen[nei] = c_nei
                    seen[n].neighbors.append(c_nei)
                    stack.append(nei)
                else:
                    seen[n].neighbors.append(seen[nei])
        return c_node