class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i, (a,b) in enumerate(edges):
            adj[a].append((b,succProb[i]))
            adj[b].append((a,succProb[i]))
        
        visit = set()
        maxHeap = [(-1.0, start_node)]
        
        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            prob = -prob
            if node == end_node:
                return prob
            if node in visit:
                continue
            visit.add(node)
            for e, p in adj[node]:
                if e not in visit:
                    heapq.heappush(maxHeap, [-1*prob*p, e])
        return 0.0