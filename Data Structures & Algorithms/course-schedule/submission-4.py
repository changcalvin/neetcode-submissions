class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## METHOD2: TOPOLOGICAL SORT + INDEGREE

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
        
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1
                
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return completed == numCourses

        ## time
            # graph: O(V + E)
            # queue: O(V)
        ## TOTAL: O(V + E)

        ## space
            # adjacency list: O(V + E)
            # indegree: O(V)
            # queue: O(V)
        ## TOTAL: O(V + E)

        