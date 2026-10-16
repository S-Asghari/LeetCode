class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        def backtrack(built, left):
            if not left:
                res.append(built)
                return
            
            prev_num = -11 # out of bound
            for i in range(len(left)):
                num = left[i]
                if num == prev_num: continue
                backtrack(built + [num], left[:i] + left[i+1:])
                prev_num = num

        backtrack([], nums)
        return res