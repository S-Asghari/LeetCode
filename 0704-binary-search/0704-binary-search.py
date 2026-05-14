class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findTarget(l, r):
            if r-l < 2:
                if target == nums[l]:
                    return l
                elif target == nums[r]:
                    return r
                else:
                    return -1
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return findTarget(l, mid)
            else: # target > nums[mid]
                return findTarget(mid+1, r)

        n = len(nums)
        return findTarget(0, n-1)