class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        instability = [0] * len(nums)
        
        # Find prefix max for all indexes (traversing from left to right)
        prefixMax = float("-inf")
        for i in range(len(nums)):
            prefixMax = max(prefixMax, nums[i])
            instability[i] = prefixMax
        
        # Find suffix min for all indexes (traversing from right to left)
        suffixMin = float("inf")
        minStable = len(nums)
        for i in range(len(nums)-1, -1, -1):
            suffixMin = min(suffixMin, nums[i])
            instability[i] -= suffixMin
            if instability[i] <= k:
                minStable = min(minStable, i)
        
        return minStable if minStable < len(nums) else -1