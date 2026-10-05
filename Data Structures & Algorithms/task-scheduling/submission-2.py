class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## heap
        # 每种 task 的出现次数
        count = Counter(tasks)
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)

        # queue: [剩余次数, 可以重新使用的时间]
        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1

            # 当前有可以执行的 task
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                freq += 1  # 例如 -3 -> -2，表示还剩 2 次

                # 如果还有剩余，进入 cooldown
                if freq < 0:
                    queue.append((freq, time + n))

            # cooldown 结束，重新放回 heap
            if queue and queue[0][1] == time:
                freq, ready_time = queue.popleft()
                heapq.heappush(maxHeap, freq)

        return time
