class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        ## method1: Modified Dijkstra + Max Heap


        # 建立无向图：
        # graph[u] = [(v, probability), ...]
        graph = defaultdict(list)

        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]

            graph[u].append((v, prob))
            graph[v].append((u, prob))

        # max_prob[i] 表示：
        # 目前找到的从 start 到 i 的最大成功概率
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        # Python 只有 min heap，所以存负概率来模拟 max heap
        # heap 中保存 (-当前成功概率, node)
        max_heap = [(-1.0, start_node)]

        while max_heap:
            neg_prob, node = heapq.heappop(max_heap)
            cur_prob = -neg_prob

            # 如果这是 heap 中旧的、更差的状态，直接跳过
            if cur_prob < max_prob[node]:
                continue

            # 当前是剩余节点中概率最大的，
            # 第一次到达终点时就是最终答案
            if node == end_node:
                return cur_prob

            for nei, edge_prob in graph[node]:
                # 路径概率是沿途所有边概率的乘积
                new_prob = cur_prob * edge_prob

                # 找到一条成功概率更高的路径
                if new_prob > max_prob[nei]:
                    max_prob[nei] = new_prob

                    # 新的更优状态需要重新加入 heap，
                    # 之后继续用它更新邻居
                    heapq.heappush(
                        max_heap,
                        (-new_prob, nei)
                    )

        # end 无法从 start 到达
        return 0.0