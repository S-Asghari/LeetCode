class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        repeated, missing = 0, 0
        numsDict = dict.fromkeys(range(1, n+1), False)
        for num in nums:
            if not numsDict[num]: numsDict[num] = True
            else: repeated = num
        for num in numsDict:
            if not numsDict[num]: 
                missing = num
                break
        return [repeated, missing]