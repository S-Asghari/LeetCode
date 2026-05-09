class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # 1. Sort the array
        # 2. Find the number of occurances for each value
        # 3. Return the weighted sum
        
        # n = len(nums)
        # min_val = float('inf')
        # min_count = 0
        # for num in nums:
        #     if num < min_val:
        #         min_val = num
        #         min_count = 1
        #     elif num == min_val:
        #         min_count += 1

        # if n == min_count:
        #     return 0
        # else:
        #     return n - min_count + 1
        nums.sort()
        operations = 0
        current_val = nums[0]
        current_level = 0
        idx = 1
        while idx < len(nums):
            if nums[idx] > current_val:
                current_val = nums[idx]
                current_level += 1
            operations += current_level
            idx += 1

        return operations
        