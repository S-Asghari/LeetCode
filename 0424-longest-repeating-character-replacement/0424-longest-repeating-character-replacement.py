class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s = "BABBAB", k = 2
        def maxCount(count):
            m = 0
            for c in count:
                if count[c] > m:
                    m = count[c]
            return m

        l = 0
        r = 0
        count = {}
        result = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            isValid = True if (r-l+1) - maxCount(count) <= k else False
            if isValid:
                result = max(result, r-l+1)
            else:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            r += 1

        return result