class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        path = []

        def backtrack(i):
            # 所有 digit 都已经选完
            if i == len(digits):
                res.append("".join(path))
                return

            # 当前 digit 对应的每个字母都尝试一次
            for ch in mapping[digits[i]]:
                path.append(ch)      # 选择
                backtrack(i + 1)       # 处理下一个 digit
                path.pop()             # 撤销选择

        backtrack(0)
        return res   

# Time: O(n * 4^n)
# Space: O(n)  # recursion + path, excluding output