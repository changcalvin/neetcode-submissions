class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        queue = deque()

        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        grid[nr][nc] != 1
                    ):
                        continue
                    
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
            
            minutes += 1
        
        if fresh > 0:
            return -1
        
        return minutes

        # time: O(m * n)
        # space: O(m * n)
