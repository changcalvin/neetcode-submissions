class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # res：保存插入并合并后的 intervals
        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            # 情况 1：当前 interval 完全在 newInterval 左边
            # 不重叠，直接加入结果
            if end < newInterval[0]:
                res.append(intervals[i])
            # 情况 2：当前 interval 完全在 newInterval 右边
            elif start > newInterval[1]:
                # 先加入已经合并完成的 newInterval
                res.append(newInterval)
                # 后面的 intervals 都不可能再重叠
                res.extend(intervals[i:])
                return res
            # 情况 3：两个 intervals 重叠
            else:
                # 更新 newInterval 的左右边界
                # 后续还可能继续合并
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        # 如果遍历结束仍未插入 newInterval
        # 说明它位于最后，或者一直合并到最后
        res.append(newInterval)

        return res
# Time: O(n)
# Space: O(n)