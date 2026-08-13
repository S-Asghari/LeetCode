class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)
        i = 0 # index
        while i < n // 2:
            if x[i] != x[n-1-i]:
                return False
            i += 1
        return True