class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # ans = 0
        # n = len(nums)
        # memo = [[0 for j in range(n)] for i in range(n)]
        # for i in range(n):
        #     for j in range(i, n):
        #         if i == j:
        #             memo[i][j] = nums[i]
        #         else:
        #             memo[i][j] = memo[i][j-1] + nums[j]
        #         if memo[i][j] == k:
        #             ans += 1
        # return ans
        # -------------------
        # TIME LIMIT EXCEEDED
        # -------------------
        # NeetCode's solution
        ans = 0
        prefixSums = {0:1} # key: prefix sum, value: count
        total = 0
        n = len(nums)
        
        for i in range(n):
            total += nums[i]
            if total - k in prefixSums:
                ans += prefixSums[total - k]
            if total not in prefixSums:
                prefixSums[total] = 1
            else:
                prefixSums[total] += 1
        
        return ans