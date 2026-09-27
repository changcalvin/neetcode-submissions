class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        ## method 2: Binary search 最小的t + BFS 检查是否可以达到
        ## "给定水位t，能不能到终点？"

        n = len(grid)

        def can_reach(time):
            if grid[0][0] > time:
                return False
            
            queue = deque([(0, 0)])
            visited = {(0, 0)}

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                r, c = queue.popleft()

                if r == n - 1 and c == n - 1:
                    return True
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < n
                        and 0 <= nc < n
                        and (nr, nc) not in visited
                        and grid[nr][nc] <= time
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            return False
        
        left = max(grid[0][0], grid[n - 1][n - 1])
        right = max(max(row) for row in grid)

        while left < right:
            mid = (left + right) // 2

            if can_reach(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

        