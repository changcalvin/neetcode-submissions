class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        visit.add((0,0))
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if r == N-1 and c == N-1:
                return time
            for dr, dc in directions:
                if r+dr < 0 or c+dc < 0 or r+dr == N or c+dc == N or (r+dr, c+dc) in visit:
                    continue
                visit.add((r+dr, c+dc))
                heapq.heappush(minHeap, [max(time, grid[r+dr][c+dc]), r+dr, c+dc])
        return -1

