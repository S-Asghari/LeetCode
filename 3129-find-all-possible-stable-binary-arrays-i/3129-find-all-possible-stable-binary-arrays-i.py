class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [[[0 for _ in range(2)] for _ in range(one + 1)] for _ in range(zero + 1)]
        mod = 10 ** 9 + 7
        
        for i in range(min(limit, zero) + 1):
            dp[i][0][0] = 1
        for j in range(min(limit, one) + 1):
            dp[0][j][1] = 1
        
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # If the most recent element is a zero
                if i > limit:
                    dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1] - dp[i-1-limit][j][1]
                else:
                    dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
                dp[i][j][0] %= mod

                # If the most recent element is a one
                if j > limit:
                    dp[i][j][1] = dp[i][j-1][0] + dp[i][j-1][1] - dp[i][j-1-limit][0]
                else:
                    dp[i][j][1] = dp[i][j-1][0] + dp[i][j-1][1]
                dp[i][j][1] %= mod
        
        return (dp[zero][one][0] + dp[zero][one][1]) % mod