class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max heap：保存目前距离最近的 k 个点
        # Python 是 min heap，所以用 negative distance 模拟 max heap
        heap = []

        for x, y in points:
            # 不需要 sqrt，平方距离的大小关系相同
            dist = x * x + y * y

            # 保存 (-distance, x, y)
            heapq.heappush(heap, (-dist, x, y))

            # 超过 k 个时：
            # heap top 的 negative distance 最小
            # 对应真实 distance 最大，因此删除当前最远的点
            if len(heap) > k:
                heapq.heappop(heap)

        # 题目允许任意顺序返回
        return [[x, y] for _, x, y in heap]

        # Time: O(n log k)
        # Space: O(k)