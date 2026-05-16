class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, r):
            mid = (l+r) // 2
            i = l
            j = mid+1
            new_arr = []
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    new_arr.append(nums[i])
                    i += 1
                else:
                    new_arr.append(nums[j])
                    j += 1
            new_arr += nums[i:mid+1]
            new_arr += nums[j:r+1]
            nums[l:r+1] = new_arr

        def sort(l, r):
            if l < r:
                mid = (l+r) // 2
                sort(l, mid)
                sort(mid+1, r)
                merge(l, r)
        
        n = len(nums)
        sort(0, n-1)
        return nums