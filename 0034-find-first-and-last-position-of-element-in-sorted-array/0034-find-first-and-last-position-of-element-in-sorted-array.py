class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # leftIdx, rightIdx = len(nums), -1
        
        # def findTarget(s, e, ):
        #     nonlocal leftIdx, rightIdx

        #     if s >= e:
        #         return
            
        #     mid = (s+e) // 2
            
        #     if nums[mid] > target:
        #         findTarget(s, mid) # [0, 3) 
            
        #     elif nums[mid] < target:
        #         findTarget(mid+1, e) # [3, 6)
            
        #     else: # nums[mid] == target
        #         if nums[s] == target:
        #             leftIdx = min(leftIdx, s)
        #         else:
        #             leftIdx = min(leftIdx, mid)
        #             findTarget(s+1, mid)
                
        #         if nums[e-1] == target:
        #             rightIdx = max(rightIdx, e-1)
        #         else:
        #             rightIdx = max(rightIdx, mid)
        #             findTarget(mid+1, e-1)

        # findTarget(0, len(nums)) # [0, 6)
        # if leftIdx < len(nums) and rightIdx > -1:
        #     return [leftIdx, rightIdx]
        # else:
        #     return [-1, -1]
    # -------------------
    # Restrictions Failed
    # -------------------
    # NeedCode's solution
        leftIdx = self.binarySearch(nums, target, True)
        rightIdx = self.binarySearch(nums, target, False)
        return [leftIdx, rightIdx]

    def binarySearch(self, nums, target, leftBiased):
        l, r = 0, len(nums)
        i = -1
        while l < r:
            m = (l+r)//2
            if target < nums[m]:
                r = m
            elif target > nums[m]:
                l = m+1
            else:
                i = m
                if leftBiased:
                    r = m
                else:
                    l = m+1
        return i
