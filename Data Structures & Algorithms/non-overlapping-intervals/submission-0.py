class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy：优先保留结束最早的 interval
        intervals.sort(key=lambda x: x[1])
        # 题目保证 intervals 非空，第一个 interval 一定保留
        prev_end = intervals[0][1]
        # 需要删除的 interval 数量
        res = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # 不重叠：可以保留当前 interval
            # 注意 start == prev_end 也算不重叠
            if start >= prev_end:
                prev_end = end
            else:
                # 重叠：删除当前 interval
                # prev_end 不变，因为之前的 interval 结束更早
                res += 1

        return res