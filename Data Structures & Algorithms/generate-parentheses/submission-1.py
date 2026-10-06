class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(open, close):
            # 已经用了 n 对括号
            if open == n and close == n:
                res.append("".join(path))
                return

            # 还能放左括号
            if open < n:
                path.append("(")
                backtrack(open + 1, close)
                path.pop()

            # 只有左括号更多时，才能放右括号
            if close < open:
                path.append(")")
                backtrack(open, close + 1)
                path.pop()

        backtrack(0, 0)
        return res

# Time: O(4^n / sqrt(n))
# Space: O(n)