class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {} # number: index
        result = []

        for i, num in enumerate(numbers):
            need = target - num
            if need in seen:
                result.append(seen[need] + 1)
                result.append(i + 1)
            seen[num] = i
        return result
