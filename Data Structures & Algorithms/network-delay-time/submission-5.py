class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph[u] = [(v, weight), ...]
        # 表示从 u 出发，可以到达哪些节点，以及对应 edge weight
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # dist[i]：从 source k 到节点 i 的当前最短距离
        # 节点编号是 1 ~ n，所以开 n + 1
        dist = [float("inf")] * (n + 1)
        # source 到自己的距离为 0
        dist[k] = 0
        # min heap: (distance_from_k, node)
        # 初始化只有 source
        min_heap = [(0, k)]

        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)
            # 同一个 node 可能以不同 distance 多次进入 heap
            # 如果当前取出的是旧的、更大的 distance，直接跳过
            if curr_dist > dist[node]:
                continue
            # Relax 当前 node 的所有 outgoing edges
            for neighbor, weight in graph[node]:
                new_dist = curr_dist + weight
                # 找到从 k 到 neighbor 的更短路径
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))

        # 节点编号从 1 开始，所以忽略 dist[0]
        answer = max(dist[1:])

        # 如果还有 inf，说明至少一个节点从 k 无法到达
        if answer == float("inf"):
            return -1

        return answer

        # V = n 个 nodes
        # E = len(times) 条 edges


        ## Time: O((V + E) log V)
        ## Space: O(V + E)
