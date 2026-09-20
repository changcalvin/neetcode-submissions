class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                m = manhattan(points[i], points[j])
                adj[i].append([j, m])
                adj[j].append([i, m])
        
        minHeap = []
        visit = set()
        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 1, neighbor])
        visit.add(0)
        res = 0

        while minHeap:
            w, s, d = heapq.heappop(minHeap)
            if d in visit:
                continue
            res += w
            visit.add(d)
            for neighbor, weight in adj[d]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, d, neighbor])
        return res
