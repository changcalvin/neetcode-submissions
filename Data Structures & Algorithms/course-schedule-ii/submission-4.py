class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ## METHOD1: TOPOLOGICAL SORT + INDEGREE(Kahn's Algorithm)

        # graph[pre]: 学完pre后可以解锁哪些课程
        graph = [[] for _ in range(numCourses)]

        # indegree[i]: 课程i还需要多少门prerequisite
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        if len(order) == numCourses:
            return order
        
        return []

        # V = numCourses
        # E = len(prerequisits)

        ## time
        ## TOTAL: O(V + E)

        ## space
        ## TOTAL: O(V + E)
        