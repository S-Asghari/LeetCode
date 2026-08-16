from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        count = {c:0 for c in range(26)}
        for c in s:
            key = ord(c) - ord('a')
            count[key] += 1
        
        for c in t:
            key = ord(c) - ord('a')
            if count[key] > 0:
                count[key] -= 1
            else:
                return False
        
        return True