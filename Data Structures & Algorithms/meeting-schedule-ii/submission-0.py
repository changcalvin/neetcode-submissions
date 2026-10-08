"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Optional：题目允许空数组，此时不需要会议室
        if not intervals:
            return 0

        # 按会议开始时间升序排序
        intervals.sort(key=lambda x: x.start)
        # Min Heap：存储每间会议室当前最后一个会议的结束时间
        # heap[0] 始终是最早结束的会议室
        heap = []

        for interval in intervals:
            start = interval.start
            end = interval.end
            # 最早结束的会议室已经空闲，可以复用
            # 注意 end == start 不算冲突
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            # 如果复用会议室：更新结束时间
            # 如果无法复用：相当于新开一间会议室
            heapq.heappush(heap, end)

        # Heap 中每个元素代表一间会议室
        return len(heap)

# Time: O(n log n)
# Space: O(n)
