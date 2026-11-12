class Solution:
    def trap(self, height: list[int]) -> int:
        # --------------------------------------------------------
        # Solution 1: O(n) time complexity, O(n) memory complexity
        # --------------------------------------------------------
        n = len(height)
        maxLeft = [0] * n
        maxSoFar = 0
        for i in range(n):
            maxLeft[i] = maxSoFar
            maxSoFar = max(maxSoFar, height[i])

        maxRight = [0] * n
        maxSoFar = 0
        for i in range(n - 1, -1, -1):
            maxRight[i] = maxSoFar
            maxSoFar = max(maxSoFar, height[i])

        trappedWater = 0
        for i in range(n):
            if min(maxLeft[i], maxRight[i]) - height[i] > 0:
                trappedWater += min(maxLeft[i], maxRight[i]) - height[i]

        return trappedWater