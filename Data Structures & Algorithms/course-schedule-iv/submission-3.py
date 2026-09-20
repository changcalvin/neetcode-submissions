class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        for course, prereq in prerequisites:
            adj[course].add(prereq)

        visit = set()

        def dfs(src):
            if src in visit:
                return
            visit.add(src)

            for n in list(adj[src]):
                dfs(n)
                adj[src] |= adj[n]

        for i in range(numCourses):
            dfs(i)

        res = [y in adj[x] for x, y in queries]
        return res
        

        
        
        

            
        
