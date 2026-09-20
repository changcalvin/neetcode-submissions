class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for prereq, course in prerequisites:
            adj[prereq].append(course)
        
        visit = set()
        path = set()
        topSort = []
        for i in range(numCourses):
            if not self.dfs(i, path, visit, adj, topSort):
                return []
        return topSort
    
    def dfs(self, src, path, visit, adj, topSort):
        if src in path:
            return False
        if src in visit:
            return True
        visit.add(src)
        path.add(src)

        for p in adj[src]:
            if not self.dfs(p, path, visit, adj, topSort):
                return False
        topSort.append(src)
        path.remove(src)
        return True