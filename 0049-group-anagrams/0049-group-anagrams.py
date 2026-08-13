from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s].append(s)
        
        res = []
        for k in anagrams:
            res.append(anagrams[k])
        return res