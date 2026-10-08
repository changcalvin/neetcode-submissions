class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        # 当前这一跳能够覆盖到的最远位置
        current_end = 0
        # 在当前覆盖范围内，下一跳最远可以到哪里
        farthest = 0

        # 不需要从最后一个位置继续跳
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            # 已经走到当前这一跳的边界
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps