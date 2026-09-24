class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        ## Top-down DFS + Memoization

        # memo[(i, remain)] 表示：从 coins[i:] 中凑出 remain 的组合数量
        memo = {}

        def dfs(i, remain):
            # 正好凑出目标：当前找到 1 种合法组合
            if remain == 0:
                return 1

            # coin 已经用完，或者金额超过目标
            # 当前路径不合法
            if i == len(coins) or remain < 0:
                return 0

            state = (i, remain)

            # 相同状态之前已经计算过
            if state in memo:
                return memo[state]

            # 选择 1：使用当前 coin
            # 因为 coin 可以无限使用，
            # 所以 i 不变，仍然可以继续使用当前 coin
            use = dfs(i, remain - coins[i])

            # 选择 2：不再使用当前 coin
            # 移动到下一种 coin
            skip = dfs(i + 1, remain)

            # 两类组合互不重复，所以直接相加
            memo[state] = use + skip

            return memo[state]

        return dfs(0, amount)



    # 设：C = len(coins)，A = amount

    ## Time = O(CA)
        # 状态: (i, remain)
        # i 有：O(C) 种。
        # remain 有：O(A) 种。
        # 所以最多：O(CA) 个状态。
        # 每个状态只做常数级两个递归分支。
        # 因此：Time = O(CA)

    ## Space = O(CA)
        # memo = O(CA)
        # 递归栈最坏：O(A + C)
        # 所以最终：Space = O(CA)