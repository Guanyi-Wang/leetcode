"""
Topological  sort using dfs.
Each node has three possible status: unvisited:0, visiting(visiting its neighbor):1 and visited:2
Use these status during dfs to see if there is circle in graph.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        status = [0]*numCourses
        # build graph as adjacent list
        graph = collections.defaultdict(list)
        for c, pre_c in prerequisites:
            graph[pre_c].append(c)

        def dfs(course):
            if status[course] == 1: # circle case
                print(1)
                return False
            if status[course] == 2: # visited node, return
                return True
            # if this neighbor is unvisited
            status[course] = 1  # mark as visiting during visiting its neighbor
            for c in graph[course]:
                if not dfs(c):  # return False if find circle
                    print(2)
                    return False
            status[course] = 2 # mark as visited
            return True
        for course in range(numCourses):
            if status[course] == 0:
               if not dfs(course):
                    return False
        return True