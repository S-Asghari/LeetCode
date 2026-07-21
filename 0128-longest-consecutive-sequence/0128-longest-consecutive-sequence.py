class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # NeetCode's solution
        numSet = set(nums)
        result = 0
        
        for n in numSet:
            if n-1 not in numSet: # n is the starting element of a consecutive subsequence
                length = 1
                while n+length in numSet:
                    length += 1
                result = max(result, length)

        return result
