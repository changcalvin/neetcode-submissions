class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        ## kruskal + union-find

        n = len(points)

        edges = [] #(cost, node1, node2)

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        
        edges.sort()

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False
            
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True
        
        total_cost = 0
        edges_used = 0

        for cost, u, v in edges:
            if union(u, v):
                total_cost += cost
                edges_used += 1

                if edges_used == n - 1:
                    break
        
        return total_cost

