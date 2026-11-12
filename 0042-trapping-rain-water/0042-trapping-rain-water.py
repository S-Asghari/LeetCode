class Solution:
    def trap(self, height: list[int]) -> int:
        # --------------------------------------------------------
        # Solution 1: O(n) time complexity, O(n) memory complexity
        # --------------------------------------------------------
        # n = len(height)
        # maxLeft = [0] * n
        # maxSoFar = 0
        # for i in range(n):
        #     maxLeft[i] = maxSoFar
        #     maxSoFar = max(maxSoFar, height[i])

        # maxRight = [0] * n
        # maxSoFar = 0
        # for i in range(n - 1, -1, -1):
        #     maxRight[i] = maxSoFar
        #     maxSoFar = max(maxSoFar, height[i])

        # trappedWater = 0
        # for i in range(n):
        #     if min(maxLeft[i], maxRight[i]) - height[i] > 0:
        #         trappedWater += min(maxLeft[i], maxRight[i]) - height[i]

        # return trappedWater

        # --------------------------------------------------------
        # Solution 2: O(n) time complexity, O(1) memory complexity
        # --------------------------------------------------------
        n = len(height)
        l, r = 0, n - 1 # left and right pointers
        maxLeft, maxRight = 0, 0

        trappedWater = 0

        while l <= r:
            if maxLeft <= maxRight:
                if maxLeft - height[l] > 0:
                    trappedWater += maxLeft - height[l]
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                if maxRight - height[r] > 0:
                    trappedWater += maxRight - height[r]
                maxRight = max(maxRight, height[r])
                r -= 1

        return trappedWater
