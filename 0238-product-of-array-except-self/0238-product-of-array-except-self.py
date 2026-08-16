class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # NeetCode's solution
        # ----------
        # Solution A
        # ----------
        # n = len(nums)
        # prefix, postfix = [1] * n, [1] * n
        # prefix[0], postfix[n-1] = nums[0], nums[n-1]

        # for i in range(1, n):
        #     prefix[i] = prefix[i-1] * nums[i]
        
        # for i in range(n-2, -1, -1):
        #     postfix[i] = postfix[i+1] * nums[i]
        
        # res = [1] * n
        # for i in range(n):
        #     if i > 0:
        #         res[i] *= prefix[i-1]
        #     if i < n-1:
        #         res[i] *= postfix[i+1]

        # return res
        # -----------------------------
        # Solution B: O(1) extra memory
        # -----------------------------
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res