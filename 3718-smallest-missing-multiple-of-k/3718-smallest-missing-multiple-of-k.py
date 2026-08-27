class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        multiples = set([k * i for i in range(1, n+2)])
        for num in nums:
            if num % k == 0:
                multiples.discard(num)
        return min(multiples)