class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ## Quickselect

        # 第 k 大 = ascending order 中 index n-k
        target = len(nums) - k

        left, right = 0, len(nums) - 1

        while left <= right:
            # 这里简单选择最后一个元素作为 pivot
            pivot = nums[right]

            # p 表示下一个“小于等于 pivot”的元素应该放的位置
            p = left

            # Partition：把 <= pivot 的元素移到左边
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # 把 pivot 放到最终正确的位置 p
            nums[p], nums[right] = nums[right], nums[p]

            if p == target:
                return nums[p]

            # target 在左边，只继续搜索左半边
            elif p > target:
                right = p - 1

            # target 在右边，只继续搜索右半边
            else:
                left = p + 1
            

            # Average Time: O(n)
            # 每次 partition 是线性的，但之后只进入其中一侧，因此平均 O(n)。
            # Worst Time: O(n²)
            # 如果每次 pivot 都选得很差，例如不断选到最大/最小值。

            # Space: O(1)
            # 这个 iterative 版本直接原地 partition。