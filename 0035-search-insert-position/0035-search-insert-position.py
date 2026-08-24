class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binarySearch(s, e):
            if s == e: 
                return e
            
            m = (s + e) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                return binarySearch(s, m)
            else:
                return binarySearch(m+1, e)
    
        return binarySearch(0, len(nums))