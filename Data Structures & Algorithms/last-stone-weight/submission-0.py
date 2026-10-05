class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python heapq 是 min heap
        # 取负数，把它变成 max heap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # 最重和第二重
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            # 不一样就把差值放回去
            if first != second:
                heapq.heappush(heap, -(first - second))

        # 没石头返回 0，否则返回剩下的石头
        return -heap[0] if heap else 0