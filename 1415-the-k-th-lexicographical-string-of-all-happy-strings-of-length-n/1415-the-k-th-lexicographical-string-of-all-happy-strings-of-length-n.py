class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        results = []
        characters = {'a', 'b', 'c'}
        def backtrack(cur_str):
            if len(cur_str) == n:
                results.append(cur_str)
                return
            for c in characters:
                if len(cur_str) == 0 or c != cur_str[-1]:
                    cur_str += c
                    backtrack(cur_str)
                    cur_str = cur_str[:-1]
        
        backtrack("")
        results.sort()
        return results[k-1] if k <= len(results) else ""