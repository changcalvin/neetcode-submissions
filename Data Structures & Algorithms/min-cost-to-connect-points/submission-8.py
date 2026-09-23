class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        ## prim + min_dist list
        
        n = len(points)

        min_dist = [float('inf')] * n
        min_dist[0] = 0
        
        visited = [False] * n
        
        total_cost = 0

        for _ in range(n):
            node = -1

            for i in range(n):
                if not visited[i] and (
                    node == -1 or min_dist[i] < min_dist[node]
                ):
                    node = i
            
            visited[node] = True
            total_cost += min_dist[node]

            x1, y1 = points[node]

            for nei in range(n):
                if not visited[nei]:
                    x2, y2 = points[nei]
                    dist = abs(x1 - x2) + abs(y1 - y2)

                    min_dist[nei] = min(min_dist[nei], dist)
        
        return total_cost
        