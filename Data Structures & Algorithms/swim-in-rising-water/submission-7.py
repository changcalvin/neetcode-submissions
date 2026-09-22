class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        ## method 1: shortest path / minimax path ---> Dijkstra


        # dist[r][c]: 从(0, 0)到(r, c)所需要的最小水位
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        
        dist[0][0] = grid[0][0]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        min_heap = [(grid[0][0], 0, 0)]  #(当前路径所需要的水位, row, col)

        while min_heap:
            cur_time, r, c = heapq.heappop(min_heap)

            if cur_time > dist[r][c]:
                continue
            
            if r == n - 1 and c == n - 1:
                return cur_time
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    new_time = max(cur_time, grid[nr][nc])

                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heapq.heappush(min_heap, (new_time, nr, nc))

        