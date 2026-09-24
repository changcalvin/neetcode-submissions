class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        ## Top-down DFS + Memoization
        m = len(s)
        n = len(t)

        # memo[(i, j)] 表示：用 s[i:] 匹配 t[j:] 的方案数量
        memo = {}

        def dfs(i, j):
            # Base case 1：
            # t 已经全部匹配完
            # 当前找到 1 种合法方案
            if j == n:
                return 1

            # Base case 2：
            # s 已经用完，但 t 还没有匹配完
            if i == m:
                return 0

            # 相同状态之前已经计算过
            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:
                # 选择 1：
                # 使用 s[i] 匹配 t[j]
                use = dfs(i + 1, j + 1)

                # 选择 2：
                # 不使用当前 s[i]，
                # 继续用后面的字符匹配 t[j]
                skip = dfs(i + 1, j)

                # 两种选择对应不同 subsequence，
                # 所以方案数直接相加
                result = use + skip

            else:
                # 当前字符不同，
                # s[i] 不可能用于匹配，只能跳过
                result = dfs(i + 1, j)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)

        ## Time = O(mn)
        ## Space = O(mn) + O(m) = O(mn)