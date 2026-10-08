class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}    # memo[(i, j)]：s[i:] 和 p[j:] 是否完全匹配

        def dfs(i, j):
            # Base case：pattern 已经匹配完
            # 只有 s 也匹配完，才算成功
            if j == n:
                return i == m
            # 已经计算过，直接返回
            if (i, j) in memo:
                return memo[(i, j)]
            # 当前字符是否匹配，注意先检查 i < m，避免越界
            match = i < m and (s[i] == p[j] or p[j] == '.')

            # 情况一：下一个字符是 *
            if j + 1 < n and p[j + 1] == '*':
                # 选择 1：匹配 0 次，跳过 x*
                skip = dfs(i, j + 2)
                # 选择 2：匹配至少 1 次，消耗 s 的一个字符，但 pattern 保持不变
                use = match and dfs(i + 1, j)
                res = skip or use
            else:
                # 情况二：普通字符或 .
                # 当前匹配成功，两个指针一起向后移动
                res = match and dfs(i + 1, j + 1)
            # 保存结果，避免重复计算
            memo[(i, j)] = res
            return res

        # 从两个字符串的开头开始匹配
        return dfs(0, 0)

# Space: O(mn)
# time: O(mn)