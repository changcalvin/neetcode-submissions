class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for n, c in count.items():
            heapq.heappush(heap, (-c, n))
        
        res = []
        for _ in range(k):
            val, num = heapq.heappop(heap)
            res.append(num)
        return res