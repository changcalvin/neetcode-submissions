class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 三个变量分别表示 target 的三个维度是否已经满足
        a = b = c = False

        for x, y, z in triplets:
            # 任意维度超过 target，则这个 triplet 不能使用
            # 因为 max 操作只会让数值保持不变或增大
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            # 当前 triplet 合法，检查它能提供哪些目标值
            if x == target[0]:
                a = True
            if y == target[1]:
                b = True
            if z == target[2]:
                c = True
            # 三个维度都满足，就一定可以合并成 target
            if a and b and c:
                return True
        # 遍历结束仍有维度无法满足
        return False

# Time: O(n)
# Space: O(1)