class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ## METHOD2: DFS + 3-STATE CYCLE DETECTION

        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)
        
        # 0: unvisited
        # 1: visiting: in DFS route
        # 2: visited

        state = [0] * numCourses

        order = []

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
            order.append(course)

            return True
        
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []

        return order[: : -1]


        # V = numCourses
        # E = len(prerequisites)

        ## time
            # adjacency list: O(V + E)
            # DFS: O(V + E)
        ## TOTAL: O(V + E)

        ## space
            # adjacency list: O(V + E)
            # state: O(V)
            # order: O(V)
            # DFS: worst O(V)
        ## TOTAL: O(V + E)


        