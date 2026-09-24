class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        ## Top-down DFS + Memoization
        
        # dfs(left, right) 表示：
        # s[left:right+1] 里的最长 palindromic subsequence 长度。

        memo = {}

        def dfs(left, right):
            
            # base case
            if left > right:
                return 0  # 区间为空
            
            if left == right:
                return 1  # 只剩一个字符

            state = (left, right)

            if state in memo:
                return memo[state]

            if s[left] == s[right]:
                # 两端相同，可以一起使用
                result = 2 + dfs(left + 1, right - 1)

            else:
                # 两端不同：尝试舍弃左边或舍弃右边
                skip_left = dfs(left + 1, right)
                skip_right = dfs(left, right - 1)

                result = max(skip_left, skip_right)

            memo[state] = result
            return result

        return dfs(0, len(s) - 1)

        ## Time = O(n²)
        ## Space = O(n²)