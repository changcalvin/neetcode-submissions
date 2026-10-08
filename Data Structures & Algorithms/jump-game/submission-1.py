class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # farthest：目前所有能到达的位置中，能继续延伸到的最远 index
        farthest = 0

        for i in range(len(nums)):
            # 如果当前位置都无法到达，后面的自然也无法继续探索
            if i > farthest:
                return False
            # 如果能到 i，就尝试用 i 更新最远可达位置
            farthest = max(farthest, i + nums[i])
            # 已经能到最后一个位置，可以提前结束
            # 可写可不写：只是提前终止优化
            if farthest >= len(nums) - 1:
                return True

        return True

        # Time: O(n)
        # Space: O(1)