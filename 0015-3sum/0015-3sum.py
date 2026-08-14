from collections import defaultdict

class Solution:    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # N = len(nums)
        # # twosum = {nums[i]+nums[j]: [(i, j)]}
        # twosum = defaultdict(list)
        # for i in range(N-1):
        #     for j in range(i+1, N):
        #         s = nums[i]+nums[j]
        #         twosum[s].append((i, j))
        
        # res = set()

        # for k in range(N):
        #     if -nums[k] in twosum:
        #         for i, j in twosum[-nums[k]]:
        #             if k != i and k != j:
        #                 t = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                 res.add(t)

        # return list(res)

        # -------------------
        # TIME LIMIT EXCEEDED
        # -------------------
        N = len(nums)
        nums.sort()
        res = []

        a = 0
        while a < N-2 and nums[a] <= 0:
            if a > 0 and nums[a] == nums[a-1]:
                a += 1
                continue
            b = a + 1
            c = N - 1
            while b < c:
                if nums[b] + nums[c] < -nums[a]:
                    b += 1
                elif nums[b] + nums[c] > -nums[a]:
                    c -= 1
                else:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    while nums[b] == nums[b-1] and b < c:
                        b += 1
            a += 1
        
        return res