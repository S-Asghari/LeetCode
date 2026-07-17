class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # NeetCode's solution
        result = []
        def backtrack(start, comb):
            if len(comb) == k:
                result.append(comb.copy())
                return
            
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()

        backtrack(1, [])
        return result
