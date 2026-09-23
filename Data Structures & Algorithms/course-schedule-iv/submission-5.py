class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        ## DFS/BFS

        graph = [[] for _ in range(numCourses)]

        for pre, course in prerequisites:
            graph[pre].append(course)
        
        reachable = [set() for _ in range(numCourses)]

        def dfs(start, node):
            for nei in graph[node]:
                if nei not in reachable[start]:
                    reachable[start].add(nei)
                    dfs(start, nei)
        
        for course in range(numCourses):
            dfs(course, course)
        
        ans = []

        for u, v in queries:
            ans.append(v in reachable[u])
        
        return ans

        # V: numCourses
        # E: len(prerequisites)
        # Q: len(queries)


        ## time: O(V(V + E) + Q)
        ## space: O(V^2 + E)

        