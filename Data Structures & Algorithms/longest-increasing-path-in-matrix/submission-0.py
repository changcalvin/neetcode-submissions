class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # indegree[r][c]：有多少个更小的相邻格子指向它
        indegree = [[0] * cols for _ in range(rows)]

        # Step 1：计算每个位置的 indegree
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        matrix[nr][nc] < matrix[r][c]):
                        indegree[r][c] += 1

        # Step 2：所有 indegree = 0 的位置作为起点
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if indegree[r][c] == 0:
                    q.append((r, c))

        # Step 3：BFS，每一层对应路径长度增加 1
        res = 0
        while q:
            # 当前这一层的节点数量
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # 只能沿着小值 -> 大值的方向移动
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        matrix[nr][nc] > matrix[r][c]):
                        # 删除当前节点对应的有向边
                        indegree[nr][nc] -= 1
                        # 所有更小的前驱都处理完，才能入队
                        if indegree[nr][nc] == 0:
                            q.append((nr, nc))

            # 完成一层，最长路径长度 +1
            res += 1

        return res