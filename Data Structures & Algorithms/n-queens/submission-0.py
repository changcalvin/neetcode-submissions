class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()
        pos_diag = set()  # r + c，\
        neg_diag = set()  # r - c，/

        board = [["."] * n for _ in range(n)]

        def backtrack(r): # 每一行只放一个 Queen
            # n 行都成功放完 Queen
            if r == n:
                res.append(["".join(row) for row in board])
                return

            # 尝试把当前 Queen 放在第 c 列
            for c in range(n):
                # 检查列和两条对角线
                if c in cols or r + c in pos_diag or r - c in neg_diag:
                    continue

                # 选择
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # 下一行
                backtrack(r + 1)

                # 撤销选择
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res