class Solution:
    def isPalindrome(self, x: int) -> bool:
        # --------------
        # First Solution
        # --------------
        # x = str(x)
        # n = len(x)
        # i = 0 # index
        # while i < n // 2:
        #     if x[i] != x[n-1-i]:
        #         return False
        #     i += 1
        # return True
        # ---------------
        # Second Solution
        # ---------------
        if x < 0:
            return False
        x2 = str(x)
        x2 = x2[::-1]
        x2 = int(x2)
        return True if x == x2 else False