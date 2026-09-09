class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ----------
        # Solution 1
        # ----------
        n = len(nums)
        k %= n
        # # nums[0: n] == nums[0:n-k] + nums[n-k:n]
        # nums[:] = nums[n-k:n] + nums[0:n-k]
        # ----------
        # Solution 2
        # ----------
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)