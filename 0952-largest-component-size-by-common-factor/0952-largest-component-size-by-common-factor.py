from math import floor, sqrt
from collections import defaultdict

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        label = [i for i in range(len(nums))]

        def findPrimes(n):
            range_top = floor(sqrt(n)) + 1
            for i in range(2, range_top):
                if n % i == 0:
                    return set([i]).union(findPrimes(n // i))
            return set([n])
        
        def findLabel(x):
            if label[x] != x:
                return findLabel(label[x])
            return x
        
        def unionLabels(x, y):
            x_lbl, y_lbl = findLabel(x), findLabel(y)
            label[x_lbl] = label[y_lbl] = min(x_lbl, y_lbl)
        
        primes = defaultdict(list)
        
        for i, num in enumerate(nums):
            factors = findPrimes(num)
            for f in factors:
                primes[f].append(i)

        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                unionLabels(indexes[i], indexes[i+1])

        components = {}
        largest = 0
        for idx in range(len(nums)):
            l = findLabel(idx)
            if l not in components:
                components[l] = 1
            else:
                components[l] += 1
            largest = max(largest, components[l])
        
        return largest
