class Solution:
    def reductionOperations(self, nums: List[int]) -> int:        
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
        