class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        ## Set of Reachable Sums

        total = sum(stones)
        target = total // 2

        # 当前可以组成的所有重量
        possible = {0}

        for stone in stones:
            # 当前 stone 只能用一次，
            # 所以先基于旧 possible 生成新状态
            next_possible = set(possible)

            for s in possible:
                new_sum = s + stone

                if new_sum <= target:
                    next_possible.add(new_sum)

            possible = next_possible

        best = max(possible)

        return total - 2 * best

    ## Time = O(n × target)
        # reachable sums 最多：O(target)
        # 每个 stone 都要遍历这些状态：Time = O(n × target)
    ## Space：O(target)
        # possible = O(target)
        # next_possible = O(target)
        