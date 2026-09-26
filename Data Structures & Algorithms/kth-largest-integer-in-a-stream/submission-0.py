class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k  
        self.heap = nums
        # 把传进来的参数保存到这个 KthLargest 对象里面，之后其他函数也可以继续使用。

        # 把 nums 变成 min heap
        heapq.heapify(self.heap)

        # 只保留最大的 k 个元素
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        # 加入新元素
        heapq.heappush(self.heap, val)

        # 如果超过 k 个，删除最小值
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # heap 中是最大的 k 个数
        # 其中最小的就是第 k 大
        return self.heap[0]

        
            # 假设初始有 n 个数。
            # 初始化：heapify: O(n)
            # pop 多余的 n-k 个元素: O((n-k) log n)
            # 所以可以写： Initialization: O(n + (n-k) log n)
            
            # 每次：add()
            # 最多一次 push + 一次 pop，而 heap 大小最多约 k+1：
            # Time: O(log k)
            # Space：O(k)
