class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 按照每个区间的起点从小到大排序
        intervals.sort(key=lambda x: x[0])

        merged = []

        for start, end in intervals:

            # merged 为空，或者当前区间和上一个区间不重叠
            if not merged or start > merged[-1][1]:
                merged.append([start, end])

            else:
                # 有重叠：
                # 起点不需要修改，因为排序后前一个区间起点一定更小
                # 只需要把终点扩展到两者中更大的那个
                merged[-1][1] = max(merged[-1][1], end)

        return merged

        # 假设有 n 个 intervals。
        # 排序：O(n log n)
        # 扫描一次：O(n)
        ## time：O(n log n)
        ## space：O(n)