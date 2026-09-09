class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        # nums[0: n] == nums[0:n-k] + nums[n-k:n]
        nums[:] = nums[n-k:n] + nums[0:n-k]
        