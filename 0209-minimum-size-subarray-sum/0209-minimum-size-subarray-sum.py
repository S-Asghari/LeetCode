class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        curSum = 0
        minLen = n+1
        
        while r < n:
            curSum += nums[r]
            while curSum >= target:
                minLen = min(minLen, r-l+1)
                curSum -= nums[l]
                l += 1
            r += 1
    
        return minLen if minLen != n+1 else 0
