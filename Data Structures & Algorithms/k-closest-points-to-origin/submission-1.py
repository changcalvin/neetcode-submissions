class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x * x + y * y

            # Min heap：距离最小的 point 在 heap top
            heapq.heappush(heap, (dist, x, y))

        res = []

        # 每次取出当前最近的 point
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res

        # Time: O(n + k log n) 前提是如果用 heapify 建 heap；
        # 上面逐个 heappush 的写法则是 O(n log n + k log n)。
        
        # Space: O(n)，因为所有 points 都进 heap。
        # 所以如果 k << n，我更 prefer 前面的 size-k max heap。