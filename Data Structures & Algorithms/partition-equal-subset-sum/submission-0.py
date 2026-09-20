class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        
        print(target)

        for i in range(len(nums) - 1, -1, -1):
            nextDP = dp.copy()
            for t in dp:
                nextDP.add(t + nums[i])
            dp = nextDP

        return True if target in dp else False