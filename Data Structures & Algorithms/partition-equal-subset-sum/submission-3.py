class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        ## Set of Reachable Sums
        # 维护：possible，表示目前可以组成的所有 sum。
        # 开始：possible = {0}
        # 每来一个 num：原来的 sum + 当前 num 产生新的 sum。

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        # 当前可以组成的所有 sum
        possible = {0}

        for num in nums:
            # 不能直接边遍历 possible 边修改它，
            # 所以先建立新的 set
            next_possible = set(possible)

            for s in possible:
                new_sum = s + num

                if new_sum == target:
                    return True

                if new_sum < target:
                    next_possible.add(new_sum)

            possible = next_possible

        return target in possible

        ## Time = O(n × target)
            # 最坏情况下 reachable sums 数量：O(target)
            # 每个数字都遍历这些状态
        ## Space = O(target)
            # Set 最多存：O(target)


        