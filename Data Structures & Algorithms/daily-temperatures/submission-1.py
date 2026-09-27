class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)

        # 默认没有更暖的一天，所以初始化为 0
        res = [0] * n

        # 存还没有找到 warmer day 的 index
        stack = []

        for i, temp in enumerate(temperatures):

            # 当前温度 > 栈顶那一天的温度
            # 当前 i 就是栈顶那一天遇到的第一个 warmer day
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()

                # 两个 index 的差 = 等待天数
                res[prev_day] = i - prev_day

            # 当前这一天也等待未来找到更高温度
            stack.append(i)

        return res

        # Time: O(n)
        # Space: O(n)