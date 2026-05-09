class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutive = 0
        countOnes = 0
        for i in nums:
            if i == 1:
                countOnes += 1
                maxConsecutive = max(maxConsecutive, countOnes)
            else:
                countOnes = 0
        return maxConsecutive