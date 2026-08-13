class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        src = strs[0]
        for i in range(1, len(strs)):
            if len(strs[i]) < len(src):
                src = strs[i]

        for j in range(len(src)):
            for s in strs:
                if s[j] != src[j]:
                    return src[:j]
        return src