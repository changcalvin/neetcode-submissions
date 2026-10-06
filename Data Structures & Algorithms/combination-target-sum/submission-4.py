class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []

        def dfs(i, total):
            # 找到一个合法组合
            if total == target:
                res.append(curr.copy())
                return

            # 没有数字可选，或者已经超过 target
            if i >= len(nums) or total > target:
                return

            # Choice 1：选择 nums[i]
            curr.append(nums[i])
            # 注意这里还是 i，因为 nums[i] 可以重复使用
            dfs(i, total + nums[i])
            # Backtrack
            curr.pop()
            # Choice 2：不选择 nums[i]，看下一个数字
            dfs(i + 1, total)

        dfs(0, 0)

        return res

        # 设：
            # n = len(nums)
            # T = target
            # m = min(nums)

        # Time: O(2^(T/m))，属于指数级搜索；实际复杂度还取决于 nums 和有效组合数量。
        # Auxiliary Space: O(T/m)，来自递归深度和当前 curr。