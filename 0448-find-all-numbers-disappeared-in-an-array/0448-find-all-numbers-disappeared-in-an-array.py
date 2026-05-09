class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        all_nums = set(range(1, n+1))
        available_nums = set(nums)
        return list(all_nums - available_nums)