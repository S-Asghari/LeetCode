from functools import cache

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        @cache
        def dfs(i, remaining):
            if remaining == 0:
                return True
            elif remaining < 0 or i == len(nums):
                return False
            
            return dfs(i+1, remaining - nums[i]) or dfs(i+1, remaining)
                    
        return dfs(0, total // 2)