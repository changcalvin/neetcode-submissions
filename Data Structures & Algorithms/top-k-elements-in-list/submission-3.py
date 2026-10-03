class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Step 1: 统计 frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Step 2: bucket[freq] 存所有出现 freq 次的数字
        # 最大 frequency 不可能超过 len(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        # Step 3: 从最高 frequency 往低 frequency 找
        result = []

        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)

                # 题目保证答案唯一；拿到 k 个就可以直接返回
                if len(result) == k:
                    return result

# n = len(nums)
# m = number of distinct elements，且 m <= n

# Time: O(n)
# Space: O(n)