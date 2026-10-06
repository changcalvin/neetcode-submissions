class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            # 整个字符串已经切完
            if start == len(s):
                res.append(path.copy())
                return

            # 尝试所有以 start 开头的 substring
            for end in range(start, len(s)):
                # s[start:end+1] 必须是 palindrome
                if not isPalindrome(start, end):
                    continue

                # 选择
                path.append(s[start:end + 1])
                # 下一段从 end + 1 开始
                backtrack(end + 1)
                # 撤销选择
                path.pop()

        backtrack(0)
        return res