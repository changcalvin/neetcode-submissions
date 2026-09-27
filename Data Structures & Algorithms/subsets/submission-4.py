class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ## DFS / Backtracking

        res = []
        subset = []

        def dfs(i):
            # 所有数字都已经决定选 / 不选
            if i == len(nums):
                # 必须 copy，因为 subset 后面还会继续修改
                res.append(subset.copy())
                return

            # Choice 1：选择 nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Backtrack：撤销刚才的选择
            subset.pop()

            # Choice 2：不选择 nums[i]
            dfs(i + 1)

        dfs(0)

        return res

        # Time: O(n × 2^n)
        # Output Space: O(n × 2^n)
        # 如果不算返回结果，递归深度最多 n，subset 最多也有 n 个元素：
        # Auxiliary Space: O(n)