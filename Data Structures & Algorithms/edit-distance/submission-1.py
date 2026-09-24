class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        ## Top-down DFS + Memoization

        m = len(word1)
        n = len(word2)

        # memo[(i, j)] 表示：
        # 把 word1[i:] 转换成 word2[j:]
        # 所需的最少操作数
        memo = {}

        def dfs(i, j):
            # word1 已经走完：
            # 只能把 word2 剩余字符全部插入
            if i == m:
                return n - j

            # word2 已经走完：
            # 只能把 word1 剩余字符全部删除
            if j == n:
                return m - i

            # 相同状态之前已经计算过
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                # 当前字符相同，不需要任何操作
                result = dfs(i + 1, j + 1)

            else:
                # 删除 word1[i]：
                # word1 往后走，word2 不动
                delete = dfs(i + 1, j)

                # 插入 word2[j]：
                # 相当于 word2[j] 已经匹配，
                # 但 word1[i] 还没处理
                insert = dfs(i, j + 1)

                # 替换：
                # 两边当前字符都处理完
                replace = dfs(i + 1, j + 1)

                # 三种操作都需要先花 1 次操作
                result = 1 + min(
                    delete,
                    insert,
                    replace
                )

            memo[(i, j)] = result
            return result

        return dfs(0, 0)

        ## Time = O(mn)
        ## Space = O(mn)
        