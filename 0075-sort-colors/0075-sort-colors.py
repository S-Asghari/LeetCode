class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # -------------
        # Counting Sort
        # -------------
        # colors = [0] * 3
        # for num in nums:
        #     colors[num] += 1
        
        # i, j = 0, 0
        # while i < len(nums):
        #     if colors[j] > 0:
        #         nums[i] = j
        #         i += 1
        #         colors[j] -= 1
        #     else:
        #         j += 1

        # return nums

        # ----------
        # Quick Sort
        # ----------
        l, r = 0, len(nums)-1
        i = 0

        while i <= r:
            # partition value = 1
            if nums[i] < 1:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[i] > 1:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1 # Don't increament i
            i += 1

        return nums