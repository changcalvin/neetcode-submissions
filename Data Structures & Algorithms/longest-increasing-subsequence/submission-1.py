class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[k] = 长度为 k+1 的递增 subsequence 中，最小的结尾数字
        tails = []

        for num in nums:
            # 找 tails 中第一个 >= num 的位置
            left, right = 0, len(tails)

            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            # num 比 tails 所有元素都大
            if left == len(tails):
                tails.append(num)
            else:
                # 用更小的 num 优化这个长度的结尾
                tails[left] = num

        return len(tails)