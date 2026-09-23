class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # reachable[i][j]: i是否是j的direct/undirect prerequisite
        reachable = [[False] * numCourses for _ in range(numCourses)]

        for pre, course in prerequisites:
            reachable[pre][course] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                if not reachable[i][k]:
                    continue
                
                for j in range(numCourses):
                    if reachable[k][j]:
                        reachable[i][j] = True
        
        ans = []

        for u, v in queries:
            ans.append(reachable[u][v])
        
        return ans

        # V: numCourses
        # E: len(prerequisites)
        # Q: len(queries)

        ## time
            # reachable: O(V^2)
            # 加入prerequisites: O(E)
            # ijk: O(V^3)
            # queries: O(Q)
        ## TOTAL: O (V^3 + E + Q)

        ## space
        # reachable: O(V^2)
        # answer: O(Q)
        ## TOTAL: O (V^2 + Q)



        