class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 两个 pointer 从最远的两端开始，此时 width 最大
        left, right = 0, len(heights) - 1

        max_area = 0

        while left < right:
            # 容器高度由较短的一侧决定
            current_height = min(heights[left], heights[right])

            # 两根线之间的水平距离
            current_width = right - left

            current_area = current_height * current_width
            max_area = max(max_area, current_area)

            # width 下一步一定会减小。
            # 因此只有丢掉较短的一侧，才有可能找到更高的瓶颈，
            # 从而得到更大的 area。
            if heights[left] < heights[right]:
                left += 1
            else:
                # 两边相等时移动任意一边都可以
                right -= 1

        return max_area