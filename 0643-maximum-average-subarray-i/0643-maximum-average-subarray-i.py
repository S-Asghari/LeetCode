class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curSum = sum(nums[0:k])
        maxSum = curSum
        i = 1
        while i <= n - k:
            curSum = curSum - nums[i-1] + nums[i+k-1]
            maxSum = max(maxSum, curSum)
            i += 1
        return maxSum / k