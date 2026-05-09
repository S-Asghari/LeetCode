class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub_s = ""
        for i in range(1, len(s) // 2 + 1):
            # print("i :", i)
            if len(s) % i != 0:
                continue
            sub_s = s[:i]
            # print("sub_s :", sub_s)
            if sub_s * (len(s) // i) == s:
                return True
        return False