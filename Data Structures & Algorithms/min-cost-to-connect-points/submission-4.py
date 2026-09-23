class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_heap = [(0, 0)] #(当前MST连接到某个新节点的cost，node)
        
        visited = set()
        
        total_cost = 0

        while len(visited) < n:
            cost, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            
            visited.add(node)
            total_cost += cost
            
            x1, y1 = points[node]

            for nei in range(n):
                if nei not in visited:
                    x2, y2 = points[nei]

                    dist = abs(x1 - x2) + abs(y1 - y2)

                    heapq.heappush(min_heap, (dist, nei))
        
        return total_cost


        