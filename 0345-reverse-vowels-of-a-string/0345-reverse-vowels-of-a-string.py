class Solution:
    def reverseVowels(self, s: str) -> str:
        # ----------
        # Solution A
        # ----------
        # vowels = set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'])
        # stack = []
        # for c in s:
        #     if c in vowels:
        #         stack.append(c)
        # new_s = []
        # for i, c in enumerate(s):
        #     if c in vowels:
        #         new_s.append(stack.pop())
        #     else:
        #         new_s.append(c)
        # return ''.join(new_s)
        # ----------
        # Solution B
        # ----------
        s = list(s)
        l, r = 0, len(s)-1
        vowels = set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'])
        while l <= r:
            while l < len(s) and s[l] not in vowels: l += 1
            while r >= 0 and s[r] not in vowels: r -= 1
            if l > r: break
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return ''.join(s)