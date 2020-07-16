class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        status = [0] * numCourses
        graph = collections.defaultdict(list)
        for c, pre in prerequisites:
            graph[pre].append(c)
        stack = []

        def dfs(course):
            if status[course] == 1:
                return False  # circle case
            if status[course] == 2:  # visited
                return True
            status[course] = 1  # visiting
            for c in graph[course]:
                if not dfs(c):
                    return False
            stack.append(course)
            status[course] = 2
            return True

        for course in range(numCourses):
            if status[course] == 0:
                if not dfs(course):
                    return []
        return stack[::-1]
