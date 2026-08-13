class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting sort
        colors = [0] * 3
        for num in nums:
            colors[num] += 1
        
        i, j = 0, 0
        while i < len(nums):
            if colors[j] > 0:
                nums[i] = j
                i += 1
                colors[j] -= 1
            else:
                j += 1

        return nums