class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1 
        
        ssCount = {c: 0 for c in tCount}
        need, have = len(tCount), 0
        bestSS, minL = [-1, -1], float("inf")
        l = 0
        
        for r, c in enumerate(s):
            ssCount[c] = ssCount.get(c, 0) + 1
            if c in tCount and ssCount[c] == tCount[c]:
                    have += 1
            while have == need:
                if r - l + 1 < minL:
                    bestSS, minL = [l, r], r - l + 1
                ssCount[s[l]] -= 1
                if s[l] in tCount and ssCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        return s[bestSS[0]: bestSS[1] + 1] if minL < float("inf") else ""