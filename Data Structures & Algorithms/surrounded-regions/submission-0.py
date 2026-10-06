class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != "O"):
                return

            # 标记：这个 O 和边界连通，不能被 capture
            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. 从左右边界的 O 开始
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        # 2. 从上下边界的 O 开始
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        # 3. 剩下的 O 都被包围；T 恢复成 O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

# Time: O(m * n)
# Space: O(m * n)  # DFS recursion stack in the worst case