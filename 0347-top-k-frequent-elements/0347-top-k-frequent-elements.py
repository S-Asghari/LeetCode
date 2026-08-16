class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ----------
        # Solution 1
        # ----------
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        # freq = [(num, count[num]) for num in count]
        # freq = sorted(freq, key = lambda x: -x[1])
        # res = [num[0] for num in freq[:k]]
        # return res
        # -------------------------------
        # Solution 2: NeetCode's solution
        # -------------------------------
        bucket = {i:[] for i in range(1, len(nums)+1)}
        for num in count:
            bucket[count[num]].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            if not k: break
            if k >= len(bucket[i]):
                res += bucket[i]
                k -= len(bucket[i])
            else:
                res += bucket[i][:k]
                k = 0
        return res