class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        freq = [(num, count[num]) for num in count]
        freq = sorted(freq, key = lambda x: -x[1])
        res = [num[0] for num in freq[:k]]
        return res