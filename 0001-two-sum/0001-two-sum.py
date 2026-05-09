class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in visited:
                return [visited[complement], i]
            else:
                visited[num] = i
        