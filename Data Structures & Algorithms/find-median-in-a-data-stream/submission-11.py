class MedianFinder:

    def __init__(self):
        # max heap
        self.bottom = []
        # min heap
        self.top = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.bottom, -num)
        heapq.heappush(self.top, -heapq.heappop(self.bottom))
        if len(self.top) > len(self.bottom) + 1:
            heapq.heappush(self.bottom, -heapq.heappop(self.top))

    def findMedian(self) -> float:
        if len(self.top) > len(self.bottom):
            return self.top[0]
        return (self.top[0] - self.bottom[0]) / 2
        
        