class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        nums_set = set(nums)
        l, total = 0, 0
        while l < len(nums):
            if l > 0 and nums[l] != nums[l-1] + 1:
                    break
            else:
                total += nums[l]       
                l += 1

        while total in nums_set:
            total += 1 
        
        return total