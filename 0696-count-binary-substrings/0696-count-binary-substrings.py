class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        
        nums = []
        prevVal = s[0]
        prevCount = 1
        
        for i, c in enumerate(s):
            if i == 0:
                continue
            if c == prevVal: 
                prevCount += 1
            else:
                nums.append(prevCount)
                prevVal, prevCount = c, 1
        nums.append(prevCount)

        for i in range(len(nums)):
            if i > 0:
                res += min(nums[i], nums[i-1])

        return res