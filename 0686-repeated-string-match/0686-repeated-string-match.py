class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeat = len(b) // len(a)
        a_prime = a * min_repeat
        i = 0
        while i < 3:
            if b in a_prime:
                return min_repeat + i
            a_prime = a_prime + a
            i += 1
        return -1