class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = []
        for row in matrix:
            tmp = []
            cur = 0
            for n in row:
                cur += n
                tmp.append(cur)
            self.prefixSum.append(tmp)
        print(self.prefixSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        cur = row1
        while cur < row2+1:
            right = self.prefixSum[cur][col2]
            left = self.prefixSum[cur][col1-1] if col1 > 0 else 0
            res += right - left
            cur += 1
            print(res)
        print('****')
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)