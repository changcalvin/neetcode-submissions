class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for prereq, course in prerequisites:
            adj[prereq].append(course)
        
        topSort = []
        visit = set()
        path = set()
        for i in range(numCourses):
            if not self.dfs(i, adj, path, visit, topSort):
                return False
        return len(topSort) == numCourses
    
    def dfs(self, src, adj, path, visit, topSort):
        if src in path:
            return False
        if src in visit:
            return True
        visit.add(src)
        path.add(src)

        for p in adj[src]:
            if not self.dfs(p, adj, path, visit, topSort):
                return False
        topSort.append(src)
        path.remove(src)
        return True