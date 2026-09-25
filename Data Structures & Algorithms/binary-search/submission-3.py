class Solution:
    def search(self, nums: List[int], target: int) -> int:

        ##  recursion

        def binary_search(left, right):
            if left > right:
                return -1
            
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                return binary_search(mid + 1, right)
            
            return binary_search(left, mid - 1)
        
        return binary_search(0, len(nums) - 1)


        ## time: O(logn)
        ## space: O(logn)

        