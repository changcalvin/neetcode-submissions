class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums = [1, 2, 3, 2, 2]
        # index   0  1  2  3  4
        # 我们规定：i → nums[i]
        
        # Phase 1: 找到环内相遇点
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]           # 走一步
            fast = nums[nums[fast]]     # 走两步

            if slow == fast:
                break
        
        # Phase 2: 找环入口
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow