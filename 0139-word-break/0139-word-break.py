class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        memo = {}

        def recurse(i):
            if i == n: return True
            if i in memo: return memo[i]

            for word in wordDict:
                if s.startswith(word, i) and recurse(i + len(word)):
                    memo[i] = True
                    return True
            
            memo[i] = False
            return False


        return recurse(0)