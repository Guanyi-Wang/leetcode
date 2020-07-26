"""
Find path, dfs.
Directed Acyclic, no visited dict needed.
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(start, path):
            if start == len(graph)-1:
                res.append(path)
            else:
                for n in graph[start]:
                    dfs(n, path+[n])
        res = []
        dfs(0, [0])
        return res