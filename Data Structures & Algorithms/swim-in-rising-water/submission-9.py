class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ## method 3: Binary search 最小的t + DFS 检查是否可以达到

        n = len(grid)

        # lower bound 至少需要覆盖起点和终点
        left = max(grid[0][0], grid[n - 1][n - 1])

        # 根据原题 elevation 范围，也可以使用 n*n - 1
        right = max(max(row) for row in grid)

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def can_reach(t):
            # 如果起点 elevation 已经超过 t，肯定无法出发
            if grid[0][0] > t:
                return False

            visited = {(0, 0)}
            stack = [(0, 0)]

            while stack:
                r, c = stack.pop()

                if r == n - 1 and c == n - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < n and
                        0 <= nc < n and
                        (nr, nc) not in visited and
                        grid[nr][nc] <= t
                    ):
                        visited.add((nr, nc))
                        stack.append((nr, nc))

            return False

        while left < right:
            mid = (left + right) // 2

            if can_reach(mid):
                # mid 已经可行，继续寻找更小的 water level
                right = mid
            else:
                # mid 不可行，答案一定更大
                left = mid + 1

        return left
    
 
    # 假设最大 elevation 为 M
    # Binary Search: O(log M) 次
    # 每次 DFS/BFS: O(n²)

    ## Time: O(n² log M)
    ## Space: O(n²)