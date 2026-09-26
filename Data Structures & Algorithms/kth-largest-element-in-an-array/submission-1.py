class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min heap：只保留目前最大的 k 个元素
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            # 如果超过 k 个，删除其中最小的
            # 因此 heap 始终只保留最大的 k 个元素
            if len(heap) > k:
                heapq.heappop(heap)

        # heap 中有最大的 k 个元素
        # min heap 的 root 就是其中最小的 = 全局第 k 大
        return heap[0]

        # Time: O(n log k)
        # Space: O(k)