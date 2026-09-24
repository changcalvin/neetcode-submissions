class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        ## Top-down DFS + Memoization
        # dfs(remain)表示：凑出 remain 还需要的最少 coin 数。
        
        # memo[remain] 表示：
        # 凑出 remain 最少需要多少个 coin
        memo = {}

        def dfs(remain):
            # Base case 1：
            # remain == 0，说明正好凑完，不需要更多 coin
            if remain == 0:
                return 0

            # Base case 2：
            # remain < 0，说明当前这条选择路径超过目标，不合法
            if remain < 0:
                return float("inf")

            # 相同 remain 之前已经计算过，直接返回
            if remain in memo:
                return memo[remain]

            # 当前状态下的最优答案
            min_coins = float("inf")

            # 尝试把每一种 coin 作为当前使用的 coin
            for coin in coins:
                # 使用当前 coin 后，
                # 剩余问题变成凑 remain - coin
                result = dfs(remain - coin)

                # 如果剩余金额可以被凑出来，
                # 当前方案需要 result + 1 个 coin
                if result != float("inf"):
                    min_coins = min(
                        min_coins,
                        result + 1
                    )

            # 记录当前 remain 的最优结果
            memo[remain] = min_coins

            return min_coins

        answer = dfs(amount)

        # 如果最终还是 inf，说明 amount 无法被凑出来
        return -1 if answer == float("inf") else answer


        ##Time = O(A × C)
            # 不同的 remain：0 ... amount → O(A)
            # 每个状态遍历所有 coins：O(C)
            # 所以：Time = O(A × C)
        ## Space：O(A)
            # memo = O(A)
            # 递归栈最深最坏：O(A)
            # 因此：Space = O(A)
