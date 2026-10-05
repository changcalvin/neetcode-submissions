class MedianFinder:

    def __init__(self):
        self.small = [] # max heap(neg)
        self.large = [] # min heap
        
    def addNum(self, num: int) -> None:
        # 1. 先放进 small
        heapq.heappush(self.small, -num)
        
        # 2. 把 small 最大的移到 large
        value = -heapq.heappop(self.small)
        heapq.heappush(self.large, value)

        # 3. 保证 small 的数量 >= large
        if len(self.large) > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        # 奇数：small 多一个
        if len(self.small) > len(self.large):
            return -self.small[0]

        # 偶数：两个堆顶平均
        return (-self.small[0] + self.large[0]) / 2

# addNum():      O(log n)
# findMedian():  O(1)
# Space:         O(n)