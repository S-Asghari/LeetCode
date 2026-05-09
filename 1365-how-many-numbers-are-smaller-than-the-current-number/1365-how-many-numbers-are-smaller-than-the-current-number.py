class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)

        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])

        nums_dict = {}
        for i in range(n):
            location, num = sorted_nums[i]
            if num not in nums_dict:
                nums_dict[num] = i

        result = []
        for num in nums:
            result.append(nums_dict[num])

        return result
