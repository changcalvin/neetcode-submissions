class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        ## METHOD1: DFS + 3-STATE CYCLE DETECTION

        # graph = [1, [2, 3]]
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)
        
        # 0: unvisited
        # 1: visiting: in DFS route
        # 2: visited

        state = [0] * numCourses

        def dfs(course):
            
            if state[course] == 1:
                return False
            
            if state[course] == 2:
                return True
            
            state[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            
            state[course] = 2
            return True
        
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False

        return True


        # V = numCourses
        # E = len(prerequisites)

        ## time
            # adjacency list: O(V + E)
            # DFS: O(V + E)
        ## TOTAL: O(V + E)

        ## space
            # adjacency list: O(V + E)
            # state: O(V)
            # DFS: worst O(V)
        ## TOTAL: O(V + E)


        