class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if 1 < k < n:
            middleNums = set(nums[1:n-1])
            greater = max(nums[0], nums[n-1])
            smaller = min(nums[0], nums[n-1])
            if greater not in middleNums and greater != smaller: return greater
            elif smaller not in middleNums and smaller != greater: return smaller
            else: return -1
        
        elif k == 1:
            count = {}
            for num in nums:
                if num not in count: count[num] = 1
                else: count[num] += 1
            sortedNum = [(num, count[num]) for num in count]
            sortedNum = sorted(sortedNum, key = lambda x: -x[0])
            i = 0
            while i < len(sortedNum) and sortedNum[i][1] > 1:
                i += 1
            return sortedNum[i][0] if i < len(sortedNum) else -1
            
        if k == n:
            return max(nums)
