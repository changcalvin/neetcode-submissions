class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ## Expand Around Center

        n = len(s)
        count = 0

        def expand(left, right):
            nonlocal count

            # 只要没有越界，并且左右字符相同，
            # 当前 s[left:right+1] 就是一个回文子串
            while (
                left >= 0
                and right < n
                and s[left] == s[right]
            ):
                # 每成功扩展一次，就找到一个新的回文子串
                count += 1

                # 继续向两边扩展
                left -= 1
                right += 1

        for i in range(n):
            # 奇数长度回文，例如 "aba"
            expand(i, i)

            # 偶数长度回文，例如 "abba"
            expand(i, i + 1)

        return count


        ## Time: O(n²)
        ## Space: O(1)