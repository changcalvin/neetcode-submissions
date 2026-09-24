class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ## sorting + two pointers

        # (value, original_index)
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()

        left, right = 0, len(arr) - 1

        while left < right:
            current_sum = arr[left][0] + arr[right][0]

            if current_sum == target:
                return sorted([arr[left][1], arr[right][1]])
            
            if current_sum < target:
                left += 1
            
            else:
                right -= 1
        
        # time: O(nlogn)
            # arr: n
            # sorting: nlogn
            # two pointers: n
        # space: O(n)
            # arr: n
            # others: 1
                

        