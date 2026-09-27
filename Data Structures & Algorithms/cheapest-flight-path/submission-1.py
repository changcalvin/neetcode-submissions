class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        ## Dijkstra + State
        
        # adjacency list:
        # graph[u] = [(v, price), ...]
        graph = [[] for _ in range(n)]

        for u, v, price in flights:
            graph[u].append((v, price))

        # (total_cost, current_node, edges_used)
        min_heap = [(0, src, 0)]

        # dist[node][edges]:
        # 使用恰好/至多对应状态的 edge 数到 node 的最佳 cost
        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        while min_heap:
            cost, node, edges_used = heapq.heappop(min_heap)

            # heap 按 cost 排序，因此第一次合法到达 dst
            # 就是满足 edge 限制的 minimum cost
            if node == dst:
                return cost

            # 最多允许 K + 1 条 edges
            if edges_used == k + 1:
                continue

            # 跳过 stale heap entry
            if cost > dist[node][edges_used]:
                continue

            for nei, price in graph[node]:
                new_cost = cost + price
                new_edges = edges_used + 1

                if new_cost < dist[nei][new_edges]:
                    dist[nei][new_edges] = new_cost
                    heapq.heappush(
                        min_heap,
                        (new_cost, nei, new_edges)
                    )

        return -1