class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 A 是较短数组，在 A 上做 binary search
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        left, right = 0, len(A)

        while left <= right:
            # i / j 表示左边分别取 A、B 多少个元素
            i = (left + right) // 2
            j = half - i

            # partition 左右的四个边界
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            # 找到正确 partition
            if Aleft <= Bright and Bleft <= Aright:
                # 奇数个元素
                if total % 2:
                    return min(Aright, Bright)

                # 偶数个元素
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # A 切得太靠右
            elif Aleft > Bright:
                right = i - 1

            # A 切得太靠左
            else:
                left = i + 1