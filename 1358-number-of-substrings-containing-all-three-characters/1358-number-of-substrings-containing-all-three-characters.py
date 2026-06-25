class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # total = 0
        # l = 0
        # r = l
        
        # while l < len(s) - 2:
        #     a, b, c = False, False, False
        #     while r < len(s):
        #         if s[r] == 'a':
        #             a = True
        #         elif s[r] == 'b':
        #             b = True
        #         else: # s[r] == 'c'
        #             c = True
        #         if a and b and c:
        #             total += len(s) - r
        #             break
        #         else:
        #             r += 1
        #     l += 1
        #     r = l
            
        # return total
        # -------------------
        # TIME LIMIT EXCEEDED
        # -------------------

        total = 0
        l = 0
        count = {}
        
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            
            while len(count) == 3:
                total += len(s) - r
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            
        return total
