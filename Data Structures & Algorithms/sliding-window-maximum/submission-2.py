class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## monotonic decreasing deque
        q = deque()
        res = []

        for right in range(len(nums)):
            # 1. 从右边删除所有 <= 当前元素的值
            # 它们以后不可能再成为 maximum
            while q and nums[q[-1]] <= nums[right]:
                q.pop()

            # 2. 加入当前元素的 index
            q.append(right)

            # 3. 如果最大值已经离开当前 window，从左边删除
            # 当前窗口左边界 = right - k + 1
            if q[0] < right - k + 1:
                q.popleft()

            # 4. window 达到大小 k 后，记录 maximum
            if right >= k - 1:
                res.append(nums[q[0]])

        return res

# Time: O(n)
# Space: O(k)