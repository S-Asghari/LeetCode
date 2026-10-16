class Solution:
    
    def compare(self, n1, n2):
        if n1 + n2 >= n2 + n1:
            return -1
        else:
            return 1

    def largestNumber(self, nums: list[int]) -> str:
        # NeetCode's solution
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        nums = sorted(nums, key = cmp_to_key(self.compare))
        if nums and nums[0] == "0":
            return "0"
        return "".join(nums)