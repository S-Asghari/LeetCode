class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        memo = [[-1 for j in range(N)] for i in range(N)]
        
        def recursiveDP(i, j):
            if memo[i][j] != -1: return memo[i][j]
            
            if i == j:
                memo[i][j] = 1
            
            elif s[i] == s[j]:
                if i+1 == j: memo[i][j] = 2
                else:
                    if memo[i+1][j-1] == -1: memo[i+1][j-1] = recursiveDP(i+1, j-1)
                    memo[i][j] = 2 + memo[i+1][j-1]
            
            else:
                if memo[i+1][j] == -1: memo[i+1][j] = recursiveDP(i+1, j)
                if memo[i][j-1] == -1: memo[i][j-1] = recursiveDP(i, j-1)
                memo[i][j] = max(memo[i+1][j], memo[i][j-1])
            
            return memo[i][j]

        return recursiveDP(0, N-1)