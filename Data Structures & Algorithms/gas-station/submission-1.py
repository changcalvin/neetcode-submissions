class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 总油量不足，不可能完成一圈
        if sum(gas) < sum(cost):
            return -1

        # start：当前候选起点
        # tank：从 start 出发的累计剩余油量
        start = 0
        tank = 0

        for i in range(len(gas)):
            # 在当前站加油，再消耗前往下一站的油量
            tank += gas[i] - cost[i]
            # 当前起点无法到达下一站
            if tank < 0:
                # [start, i] 都不可能是有效起点
                # 因此直接从 i+1 重新开始
                start = i + 1
                # 新起点的初始油量为 0
                tank = 0
        # 总油量足够，最终候选起点一定有效
        return start