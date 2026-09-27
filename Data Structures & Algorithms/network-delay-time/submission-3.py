class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        ## Alternative 1：Bellman-Ford
        # 对所有 edges 反复进行 relaxation

        # dist[i]：从 k 到 i 的当前最短距离
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        # 最短路径最多包含 n - 1 条 edge
        for _ in range(n - 1):
            updated = False

            for u, v, w in times:
                # u 本身必须已经 reachable，才能通过 u 更新 v
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True

            # Optional optimization：
            # 如果这一整轮没有任何 relaxation，
            # 后续距离也不会再改变，可以提前停止
            if not updated:
                break

        answer = max(dist[1:])

        return -1 if answer == float("inf") else answer

        ## Time: O(VE)
        ## Space: O(V)