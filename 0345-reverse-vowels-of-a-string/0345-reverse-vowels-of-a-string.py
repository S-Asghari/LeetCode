class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'])
        stack = []
        for c in s:
            if c in vowels:
                stack.append(c)
        new_s = []
        for i, c in enumerate(s):
            if c in vowels:
                new_s.append(stack.pop())
            else:
                new_s.append(c)
        return ''.join(new_s)
