class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        dic = [False for i in range(N)]
        for num in nums:
            if 1 <= num <= N:
                dic[num-1] = True
        
        for i in range(N):
            if not dic[i]:
                return i+1
        return N+1