class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = 0
        N = len(nums)
        count = [0] * (N+1)

        for i, num in enumerate(nums):
            if num == target:
                count[i+1] = count[i] + 1
            else:
                count[i+1] = count[i]

        # print(count)

        for i in range(1, N+1):
            for j in range(i, N+1):
                if count[j] - count[i-1] > (j-i+1)/2:
                    # print(f"nums[{i-1}..{j-1}]")
                    res += 1

        return res