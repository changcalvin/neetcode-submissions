class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        # 每组必须恰好有 groupSize 张牌
        # 如果总数不能整除，直接返回 False
        if n % groupSize != 0:
            return False

        # 按点数从小到大排序
        hand.sort()
        # count：记录每个数字剩余多少张牌
        count = {}
        for num in hand:
            count[num] = count.get(num, 0) + 1

        # 从最小的牌开始尝试组成连续的 group
        for num in hand:
            # 这张牌已经在之前的 group 中使用完
            if count[num] == 0:
                continue
            # num 是当前剩余的最小牌
            # 必须组成 num, num+1, ..., num+groupSize-1
            for x in range(num, num + groupSize):
                # 缺少任何一张牌，都无法组成连续 group
                if count.get(x, 0) == 0:
                    return False
                # 使用一张点数为 x 的牌
                count[x] -= 1

        # 所有牌都成功分组
        return True