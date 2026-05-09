class Solution:
    def smallestSubsequence(self, s: str) -> str:
        frequency = {}
        for c in s:
            if c not in frequency:
                frequency[c] = 1
            else:
                frequency[c] += 1
        
        seen = dict.fromkeys(frequency, False)
        stack = []
        
        for c in s:
            if not seen[c]:
                while stack and stack[-1] > c and frequency[stack[-1]] > 0:
                    seen[stack[-1]] = False
                    stack.pop()
                stack.append(c)
                frequency[c] -= 1
                seen[c] = True
            else:
                frequency[c] -= 1
            # print("frecuency:", frequency)
            # print("seen:", seen)
            # print("stack:", stack)

        return ''.join(stack)