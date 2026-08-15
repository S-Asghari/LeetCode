class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n+1)]
        for i in range(1, n+1):
            dp[i] = dp[i-1] + nums[i-1]
        # print(dp)

        res = float('-inf')
        minPrefix = 0
        for j in range(1, n+1):
            res = max(res, dp[j]- minPrefix)
            minPrefix = min(minPrefix, dp[j])

        return res