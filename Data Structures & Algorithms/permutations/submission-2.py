class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []

        def backtrack():
            # 已经选了 n 个数字，一个排列完成
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            # 每一层都重新看所有数字
            for num in nums:
                # 已经使用过的不能重复使用
                if num in permutation:
                    continue
                # 选择
                permutation.append(num)
                # 继续填下一个位置
                backtrack()
                # 撤销选择
                permutation.pop()

        backtrack()
        return res

# Time: O(n * n!)
# n! permutations, and copying each permutation takes O(n)
# Space: O(n)
# recursion depth + current permutation