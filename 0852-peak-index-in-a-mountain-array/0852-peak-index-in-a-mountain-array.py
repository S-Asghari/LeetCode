class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        def checkMiddle(l, r):
            if r - l < 2:
                return l if arr[l] > arr[r] else r

            mid = (l + r) // 2 # rounded to the left
            if arr[mid] >= arr[mid-1] and arr[mid] >= arr[mid+1]:
                return mid
            elif arr[mid] >= arr[mid-1]:
                return checkMiddle(mid+1, r)
            else: # arr[mid] >= arr[mid+1]
                return checkMiddle(l, mid)
        
        n = len(arr)
        return checkMiddle(0, n-1)