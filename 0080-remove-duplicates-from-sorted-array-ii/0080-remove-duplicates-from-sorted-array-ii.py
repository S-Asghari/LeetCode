class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 0
        c = 0 # occurance count
        
        for r in range(len(nums)):
            if nums[l] == nums[r]:
                c += 1
                continue
            if c >= 2:
                nums[l+1], nums[l+2] = nums[l], nums[r]
                l += 2
                c = 1
            elif c == 1:
                nums[l+1] = nums[r]
                l += 1
                c = 1
        
        if c >= 2:
            nums[l+1] = nums[l]
            l += 1
        
        # print(f"k = {l+1}")
        # print(f"nums = {nums}")
        return l + 1
            