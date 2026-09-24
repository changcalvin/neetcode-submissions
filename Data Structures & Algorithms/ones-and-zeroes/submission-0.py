class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        ## Top-down DFS + Memoization

        # 先统计每个字符串需要多少个 0 和 1
        counts = []

        for s in strs:
            counts.append((s.count('0'), s.count('1')))

        memo = {}

        def dfs(i, zeros_left, ones_left):
            # 从第 i 个字符串开始，在还剩这些 0/1 capacity 时，最多能选多少个。
            # 所有字符串都处理完
            if i == len(strs):
                return 0

            state = (i, zeros_left, ones_left)

            if state in memo:
                return memo[state]

            zeros, ones = counts[i]

            # 不选择当前字符串
            skip = dfs(i + 1, zeros_left, ones_left)

            take = 0
            # 只有 capacity 足够时才能选择
            if zeros <= zeros_left and ones <= ones_left:
                take = 1 + dfs(
                    i + 1,
                    zeros_left - zeros,
                    ones_left - ones
                )

            memo[state] = max(skip, take)

            return memo[state]

        return dfs(0, m, n)

        ## Time: O(Lmn)
            # L = len(strs)
            # 状态由：i, zeros_left, ones_left决定。
            # 状态数量最多：O(L × m × n) 每个状态做常数级工作。

        ## Space: O(Lmn)
            # memo = O(Lmn)
            # 递归栈 = O(L)
        