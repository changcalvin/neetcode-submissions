class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Boundary case：
        # 如果只有一个 house，直接 rob 它。
        # 这个必须单独处理，否则 nums[:-1] 和 nums[1:]
        # 都会变成空数组。
        
        if len(nums) == 1:
            return nums[0]
        
        # O(1) auxiliary space，不要传 slice，而是传 index range

        def rob_line(left, right):
            # 处理 nums[left:right]，right 不包含
            prev2 = prev1 = 0

            for i in range(left, right):
                current = max(prev2 + nums[i], prev1)
                prev2 = prev1
                prev1 = current

            return prev1

        n = len(nums)

        return max(
            rob_line(0, n - 1),  # exclude last
            rob_line(1, n)       # exclude first
        )

        ## Time:  O(n)

        ## Space:
        # prev2, prev1, current → O(1)
        # helper recursion      → none
        # 额外 array            → none

        ## Total: O(1)