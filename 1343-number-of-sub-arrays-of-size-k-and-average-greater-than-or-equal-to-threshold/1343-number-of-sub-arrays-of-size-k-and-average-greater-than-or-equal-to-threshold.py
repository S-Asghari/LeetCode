class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        result = 0
        
        if k > n:
            return result
        
        desired_sum = k * threshold
        total = 0
        r = n # pointer to the end of subarray
        total = sum(arr[r-k:r])
        
        while r-k >= 0:
            if total >= desired_sum:
                result += 1
            if r-k >= 1:
                total -= arr[r-1]
                total += arr[r-k-1]
            r -= 1
        
        return result