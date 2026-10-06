class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrack(start, remain):
            # 找到一个合法组合
            if remain == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                # 同一层跳过重复数字
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # 已排序，后面只会更大，可以直接停止
                if candidates[i] > remain:
                    break

                # 选择
                path.append(candidates[i])
                # i + 1：每个元素最多使用一次
                backtrack(i + 1, remain - candidates[i])
                # 撤销选择
                path.pop()

        backtrack(0, target)
        return res

# Time: O(n * 2^n)
# Space: O(n) auxiliary space