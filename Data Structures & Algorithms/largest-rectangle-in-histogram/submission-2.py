class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (start_index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            # 当前柱子更矮：
            # stack 顶部那些更高柱子的右边界确定了
            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                # 高度 height 可以从 index 延伸到 i - 1
                max_area = max(max_area, height * (i - index))

                # 当前较矮的柱子可以继承更早的起点
                start = index

            stack.append((start, h))

        # 剩下的柱子右边没有遇到更矮的，可以延伸到数组末尾
        n = len(heights)

        for index, height in stack:
            max_area = max(max_area, height * (n - index))

        return max_area