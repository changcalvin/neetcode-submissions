class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        ## BFS：shortest path

        # queue 中保存当前金额
        queue = deque([0])
        visited = {0}

        steps = 0

        while queue:
            # 当前这一层代表使用了 steps 个 coin
            for _ in range(len(queue)):
                current = queue.popleft()

                if current == amount:
                    return steps

                for coin in coins:
                    next_amount = current + coin

                    # 超过目标就不用继续
                    if next_amount > amount:
                        continue

                    if next_amount not in visited:
                        visited.add(next_amount)
                        queue.append(next_amount)

            steps += 1

        return -1

    ## Time = O(A × C)
        # 最多访问：A + 1 个金额状态。
        # 每个状态尝试：C 个 coins。
        # 所以：Time = O(A × C)
    ## Space：
        # queue = O(A)
        # visited = O(A)
        # 因此：Space = O(A)