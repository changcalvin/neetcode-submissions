class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1 * num)
        if (self.maxHeap and self.minHeap and (-1*self.maxHeap[0]) > self.minHeap[0]):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * val)

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap)+1:
            return -1 * self.maxHeap[0]
        elif len(self.minHeap) == len(self.maxHeap)+1:
            return self.minHeap[0]
        return ((-1*self.maxHeap[0])+self.minHeap[0])/2
        