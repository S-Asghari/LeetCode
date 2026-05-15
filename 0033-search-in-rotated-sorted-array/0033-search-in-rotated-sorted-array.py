class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findBreakingPoint(l, r):
            if r - l < 2:
                return l if nums[l] > nums[r] else r
    
            if nums[l] > nums[r]:
                mid = (l+r) // 2
                if nums[l] > nums[mid]:
                    return findBreakingPoint(l, mid)
                else: # nums[mid] > nums[r]
                    return findBreakingPoint(mid, r)
            else:
                return r

        
        def findTarget(l, r):
            if  r - l < 2:
                if target == nums[l]:
                    return l
                elif target == nums[r]:
                    return r
                else:
                    return -1
            
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return findTarget(l, mid-1)
            else: # target > nums[mid]
                return findTarget(mid+1, r)
        
        
        n = len(nums)
        max_idx = findBreakingPoint(0, n-1)
        nums = nums[max_idx+1:n] + nums[0:max_idx+1]
        
        target_idx = findTarget(0, n-1)
        
        if target_idx == -1:
            return -1
        else:
            if target >= nums[n-1-max_idx]:
                return target_idx - (n - (max_idx+1))
            else:
                return target_idx + (max_idx+1)