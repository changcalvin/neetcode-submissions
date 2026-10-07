class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford 有一个特别适合这题的性质：
        # 做第 i 轮 relaxation 后，
        # 可以得到最多使用 i 条 edges 的 shortest distance。

        # dist[i] = 在当前允许的 edge 数量下，
        # 从 src 到 airport i 的最小 cost
        dist = [float("inf")] * n
        # base case：src 到自己不需要任何 flight，cost = 0
        dist[src] = 0

        # K 个 stops = 最多 K + 1 条 edges
        for _ in range(k + 1):
            # 关键：这一轮的更新不能影响这一轮后面的 relaxation
            # 否则一轮可能走多条 edge，破坏 K-stop 限制
            temp = dist.copy()
            # 尝试 relax 每一条 flight
            for u, v, price in flights:
                # 如果上一轮还无法到达 u，就不能通过 u -> v 更新 v
                if dist[u] == float("inf"):
                    continue
                # relaxation：从 src -> u，再走 u -> v
                new_cost = dist[u] + price
                if new_cost < temp[v]:
                    temp[v] = new_cost
            # 完成这一轮后，再统一更新 dist
            dist = temp

        # 如果 dst 仍不可达，返回 -1
        return -1 if dist[dst] == float("inf") else dist[dst]

        # V = n airports
        # E = number of flights

        # Time: O((K + 1)(E + V))
        # Space: O(V)
