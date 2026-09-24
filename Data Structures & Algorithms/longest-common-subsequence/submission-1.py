class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ## Top-down DFS + Memoization

        m = len(text1)
        n = len(text2)

        # memo[(i, j)] 表示：
        # text1[i:] 和 text2[j:] 的 LCS 长度
        memo = {}

        def dfs(i, j):
            # Base case：
            # 任意一个字符串已经走完，
            # 后面不可能再有公共字符
            if i == m or j == n:
                return 0

            # 相同状态之前已经计算过
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                # 当前字符相同：
                # 把它加入 LCS，
                # 两边一起往后移动
                result = 1 + dfs(i + 1, j + 1)

            else:
                # 当前字符不同：
                # 选择跳过 text1[i]
                skip_text1 = dfs(i + 1, j)

                # 或者跳过 text2[j]
                skip_text2 = dfs(i, j + 1)

                # 取更长的公共子序列
                result = max(
                    skip_text1,
                    skip_text2
                )

            memo[(i, j)] = result
            return result

        return dfs(0, 0)

    ## Time = O(mn)
        # 状态：(i, j)，一共有 O(mn) 种不同状态。
        # 每个状态只计算一次：Time = O(mn)

    # Space = O(mn)
        # memo = O(mn)
        # 递归栈最深时：i 最多增加 m 次，j 最多增加 n 次
        # 所以：recursion stack = O(m + n)
        # 最终：Space = O(mn)



