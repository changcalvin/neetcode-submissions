class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        ## prim + min_dist list
        
        n = len(points)

        # min_dist[i]:
        # 当前 MST 连接到 node i 的最小 edge cost
        min_dist = [float("inf")] * n

        # 可以从任意节点开始
        # node 0 作为起点，不需要 edge，所以 cost = 0
        min_dist[0] = 0

        # visited[i] = True 表示 node i 已经加入 MST
        visited = [False] * n

        total_cost = 0

        # MST 最终需要包含全部 n 个节点
        for _ in range(n):

            # 1. 在所有未加入 MST 的节点中，
            # 找 min_dist 最小的那个
            next_node = -1
            best_dist = float("inf")

            for i in range(n):
                if not visited[i] and min_dist[i] < best_dist:
                    best_dist = min_dist[i]
                    next_node = i

            # 2. 把这个节点正式加入 MST
            visited[next_node] = True
            total_cost += min_dist[next_node]

            x1, y1 = points[next_node]

            # 3. 新节点进入 MST 后，
            # 尝试更新 MST 到其他未访问节点的最小连接成本
            for nei in range(n):
                if not visited[nei]:
                    x2, y2 = points[nei]

                    # 当前新节点 → nei 的 edge cost
                    dist = abs(x1 - x2) + abs(y1 - y2)

                    # 如果通过新加入的节点连接 nei 更便宜，
                    # 更新 nei 的最小连接成本
                    min_dist[nei] = min(min_dist[nei], dist)

        return total_cost

        ## time: O(n²)
        ## space: O(n)
        