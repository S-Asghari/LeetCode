class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # NeetCode's solution
        n = len(nums)
        total = nums[0]
        curMax, globalMax = nums[0], nums[0]
        curMin, globalMin = nums[0], nums[0]

        for i in range(1, n):
            total += nums[i]
            curMax = max(nums[i], curMax + nums[i])
            globalMax = max(globalMax, curMax)
            curMin = min(nums[i], curMin + nums[i])
            globalMin = min(globalMin, curMin)
        
        if globalMax < 0: return globalMax
        else: return max(globalMax, total - globalMin)