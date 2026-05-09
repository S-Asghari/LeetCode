class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Find the sum for all subarrays that start with idx = 0.
        # If the good subarray is not among them, remove nums[0] from all calculated sums and check again...
        # n = len(nums)
        # visited = [nums[0]]
        # cur_sum = nums[0]
        # for i in range(1, n):
        #     cur_sum += nums[i]
        #     if cur_sum % k == 0:
        #         return True
        #     visited.append(cur_sum)

        # m = len(visited)
        # for i in range(0, m-2):
        #     for j in range(i+2, m):
        #         if (visited[j] - visited[i]) % k == 0:
        #             return True
                
        # return False
        # ----------------------------------------------
        # Time Limit Exceeded. 95 / 102 testcases passed
        # ----------------------------------------------

        # NeetCode Solution:
        remainder = {0: -1}
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] >= 2:
                return True
        
        return False