class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        res = 0
        mapping = {}
        even, odd = 0, 0
        for i, n in enumerate(nums):
            mapping[i] = (even, odd)
            if i % 2 == 0: even += n
            else: odd += n
        
        for i, n in enumerate(nums):
            if i % 2 == 0:
                cur_even = odd - mapping[i][1] + mapping[i][0]
                cur_odd = even - n - mapping[i][0] + mapping[i][1]
            else:
                cur_even = odd - n - mapping[i][1] + mapping[i][0]
                cur_odd = even - mapping[i][0] + mapping[i][1]
            if cur_even == cur_odd:
                res += 1

        return res