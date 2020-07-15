"""
Disjoin Set Union
"""


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # list to store parent(root) of vetex
        parent = [-1] * len(edges)

        def find(x):
            """
            Function to find the root of a given vetex
            """
            if parent[x] == -1:  # this is a root
                return x
            else:
                parent[x] = find(parent[x])  # find root recursively
                return parent[x]

        def union(x, y):
            """
            Function to connect two vetex, return True if two were already connected.
            """
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:  # has same root,  connected
                return True
            parent[root_x] = root_y  # connect x to y, make y as root
            return False

        for x, y in edges:
            if union(x - 1, y - 1):
                return [x, y]
"""
build graph by add edges
find [u,v] in edges already connected before add into graph
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        def dfs(u, v):
            """
            return True if u and v is connected in graph.
            """
            if u not in seen:
                seen.add(u)
                if u == v:
                    return True
                return any(dfs(n,v) for n in graph[u])
        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u,v):
                return [u,v]
            graph[u].append(v)
            graph[v].append(u)