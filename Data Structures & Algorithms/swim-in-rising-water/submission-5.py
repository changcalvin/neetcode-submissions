class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        # method 3: union find  “随着水位上升，哪些格子开始联通？”

        n = len(grid)

        def index(r, c):
            return r * n + c
        
        parent = list(range(n * n))
        rank = [0] * (n * n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return
            
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
        
        cells = []
        for r in range(n):
            for c in range(n):
                cells.append((grid[r][c], r, c))
        
        cells.sort()

        opened = [[False] * n for _ in range(n)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for height, r, c in cells:
            opened[r][c] = True

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and opened[nr][nc]
                ):
                    union(index(r, c), index(nr, nc))
            
            start = index(0, 0)
            end = index(n - 1, n - 1)

            if find(start) == find(end):
                return height



