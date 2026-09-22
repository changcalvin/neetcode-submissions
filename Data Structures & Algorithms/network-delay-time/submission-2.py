class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # adjacency list: graph[u] = [(v, weight), ...]
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        min_heap = [(0, k)] #(distance, source)

        while min_heap:
            cur_dist, node = heapq.heappop(min_heap)
            if cur_dist > dist[node]:
                continue
            for nei, weight in graph[node]:
                new_dist = cur_dist + weight

                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(min_heap, (new_dist, nei))
                
        max_dist = max(dist[1:])
        
        return max_dist if max_dist != float('inf') else -1
        
        