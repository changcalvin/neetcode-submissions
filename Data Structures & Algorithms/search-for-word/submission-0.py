class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # 整个 word 都匹配完了
            if i == len(word): # i = 当前正在寻找 word[i]
                return True

            # 越界 or 字符不匹配
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[i]):
                return False

            # 标记当前格子已经使用
            temp = board[r][c]
            board[r][c] = "#"

            # 上下左右继续找下一个字符
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # backtrack：恢复当前格子
            board[r][c] = temp

            return found

        # 每个格子都可能是 word 的起点
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

# m = rows
# n = cols
# L = len(word)

# Time: O(m * n * 3^L)
# Space: O(L)