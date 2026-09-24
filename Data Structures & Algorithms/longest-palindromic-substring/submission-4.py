class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ## Expand Around Center

        n = len(s)

        def expand(left, right):
            # 从中心向两边扩展，只要左右字符相同，就继续扩大回文范围
            while (
                left >= 0
                and right < n
                and s[left] == s[right]
            ):
                left -= 1
                right += 1

            # 循环结束时，left 和 right 已经多走了一步
            # 所以真正的回文范围是 [left + 1, right - 1]
            return left + 1, right - 1
        
        # 记录当前最长回文子串的左右边界
        best_left = 0
        best_right = 0

        for i in range(n):
            # 情况 1：奇数长度回文
            # 例如 "aba"，中心是 i
            left1, right1 = expand(i, i)

            if right1 - left1 > best_right - best_left:
                best_left = left1
                best_right = right1

            # 情况 2：偶数长度回文
            # 例如 "abba"，中心在 i 和 i+1 之间
            left2, right2 = expand(i, i + 1)

            if right2 - left2 > best_right - best_left:
                best_left = left2
                best_right = right2

        # Python slicing 的右边界不包含，所以要写 best_right + 1
        return s[best_left:best_right + 1]

        ## Time: O(n²)
        ## Space: O(1)