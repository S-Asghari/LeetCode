class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        cache = {}

        def dfs(i, d, curMax):
            if i == len(jobDifficulty):
                return 0 if d == 0 else float("inf")
            if d == 0:
                return float("inf")
            
            if (i, d, curMax) in cache:
                return cache[(i, d, curMax)]
            
            curMax = max(curMax, jobDifficulty[i])
            res = min(
                dfs(i + 1, d, curMax), # continue with the current day
                curMax + dfs(i + 1, d - 1, -1) # end the current day
            )
            cache[(i, d, curMax)] = res
            return res

        return dfs(0, d, -1)