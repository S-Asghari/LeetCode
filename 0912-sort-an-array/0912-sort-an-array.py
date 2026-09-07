class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, r):
            m = (l+r) // 2
            i, j = l, m
            new_arr = []
            while i < m and j < r:
                if nums[i] <= nums[j]:
                    new_arr.append(nums[i])
                    i += 1
                else:
                    new_arr.append(nums[j])
                    j += 1
            if i < m: new_arr += nums[i:m]
            elif j < r: new_arr += nums[j:r]
            nums[l:r] = new_arr

        def sort(l, r):
            if r - l > 1:
                m = (l+r) // 2
                sort(l, m)
                sort(m, r)
                merge(l, r)

        sort(0, len(nums))
        return nums