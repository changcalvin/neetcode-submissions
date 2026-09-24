class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target > matrix[i][-1]:
                continue
            left = 0
            right = len(matrix[0])
            while left < right:
                mid = (left+right)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return False
        return False