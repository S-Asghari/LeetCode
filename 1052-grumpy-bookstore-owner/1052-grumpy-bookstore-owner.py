class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(grumpy)
        not_satisfied = [customers[i] * grumpy[i] for i in range(n)]
        r = n # pointer to the end of the current window
        total = sum(not_satisfied[r-minutes:r])
        max_benefit = total
        
        while r-minutes >= 0:
            max_benefit = max(max_benefit, total)
            if r-minutes >= 1:
                total -= not_satisfied[r-1]
                total += not_satisfied[r-minutes-1]
            r -= 1

        not_satisfied_count = sum(not_satisfied) - max_benefit
        satisfied_count = sum(customers) - not_satisfied_count
        return satisfied_count