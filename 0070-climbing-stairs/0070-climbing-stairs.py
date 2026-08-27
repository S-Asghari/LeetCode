class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        if n >= 2: dp[2] = 2
        i = 3 
        while i <= n:
            dp[i] = dp[i-1] + dp[i-2]
            i += 1
        return dp[n]