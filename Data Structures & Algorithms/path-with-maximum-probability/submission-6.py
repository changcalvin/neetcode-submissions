class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        ## Bellman-Ford Style Relaxation

        # prob[i] 表示目前找到的从 start 到 i 的最大成功概率
        prob = [0.0] * n
        prob[start_node] = 1.0

        # 最优 simple path 最多包含 V - 1 条边
        for _ in range(n - 1):
            updated = False

            for i in range(len(edges)):
                u, v = edges[i]
                edge_prob = succProb[i]

                # 尝试通过 u 更新 v
                if prob[u] * edge_prob > prob[v]:
                    prob[v] = prob[u] * edge_prob
                    updated = True

                # 无向图，也要尝试通过 v 更新 u
                if prob[v] * edge_prob > prob[u]:
                    prob[u] = prob[v] * edge_prob
                    updated = True

            # 如果整轮没有更新，可以提前停止
            if not updated:
                break

        return prob[end_node]
        