class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        ## Top-down DFS + Memoization
        
        m = len(s1)
        n = len(s2)

        # 长度不同一定无法组成
        if m + n != len(s3):
            return False

        # memo[(i, j)] 表示：s1[i:] 和 s2[j:]能否组成 s3[i+j:]
        memo = {}

        def dfs(i, j):
            # 两个字符串都用完，说明 s3 也正好用完
            if i == m and j == n:
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            # 尝试从 s1 取当前字符
            if (
                i < m
                and s1[i] == s3[i + j]
                and dfs(i + 1, j)
            ):
                memo[(i, j)] = True
                return True

            # 尝试从 s2 取当前字符
            if (
                j < n
                and s2[j] == s3[i + j]
                and dfs(i, j + 1)
            ):
                memo[(i, j)] = True
                return True

            # 两种选择都失败
            memo[(i, j)] = False
            return False

        return dfs(0, 0)

        ## Time = O(mn)
        ## Space = O(mn)
        