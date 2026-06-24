class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # total = sum(nums[0:3])
        
        # for i in range(0, n-1):
        #     for j in range(i+1, n):
        #         # print(f"nums[i]:{nums[i]}, nums[j]:{nums[j]}")
        #         partial_sum = nums[i] + nums[j]
        #         remaining = target - partial_sum
        #         min_dif = float('inf')
        #         min_dif_idx = -1
        #         for k in range(n):
        #             if k != i and k != j:
        #                 if abs(nums[k] - remaining) < min_dif:
        #                     min_dif = abs(nums[k] - remaining)
        #                     min_dif_idx = k
        #         # print(f"nums[min_dif_idx]:{nums[min_dif_idx]}")
        #         if abs(partial_sum + nums[min_dif_idx] - target) < abs(total - target):
        #             total = partial_sum + nums[min_dif_idx]
        
        # return total
        
        # ---------------------
        # TIME LIMIT EXCEEDED!
        # ---------------------
        
        n = len(nums)
        nums.sort()
        closest = float('inf')
        
        for i in range(n-2):
            lo = i+1
            hi = n-1
            while hi > lo:
                s = nums[i] + nums[lo] + nums[hi]
                if abs(target - s) < abs(target - closest):
                    closest = s
                    if closest == target: return closest
                if s < target: lo += 1
                elif s > target: hi -= 1
        
        return closest
