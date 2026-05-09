class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p
        
        if remain == 0:
            return 0

        res = len(nums)
        prefix_to_idx = {0: -1}

        cur_sum = 0
        for i, n in enumerate(nums):
            cur_sum += n
            cur_sum %= p
            prefix = (cur_sum - remain + p) % p
            if prefix in prefix_to_idx:
                idx = prefix_to_idx[prefix]
                res = min(res, i - idx)
            prefix_to_idx[cur_sum] = i 

        if res == len(nums):
            return -1
        return res