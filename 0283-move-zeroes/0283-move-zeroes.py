class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        z = 0
        for i in range(n):
            if nums[i] == 0:
                z += 1
            if nums[i] != 0:
                nums[i-z] = nums[i]
        for i in range(n-z, n):
            nums[i] = 0