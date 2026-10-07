class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        res = -1

        for n in nums:
            heapq.heappush(heap, -n)
        
        for _ in range(k):
            res = heapq.heappop(heap)
        
        return -res