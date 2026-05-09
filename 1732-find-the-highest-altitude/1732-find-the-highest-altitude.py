class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain) + 1
        altitudes = [float('-inf') for i in range(N)]
        altitudes[0] = 0
        maxAlt = 0
        for i in range(1, N):
            altitudes[i] = gain[i-1] + altitudes[i-1]
            maxAlt = max(maxAlt, altitudes[i])
        # print(altitudes)
        return maxAlt
