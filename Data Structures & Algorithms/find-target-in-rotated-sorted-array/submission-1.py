class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        # step 1: find the minimum element (rotation pivot)

        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left

        # step 2: find target in which sorted section

        if nums[pivot] <= target <= nums[n - 1]:
            left, right = pivot, n - 1
        else:
            left, right = 0, pivot - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

        ## time: O(logn)
        ## space: O(1)
