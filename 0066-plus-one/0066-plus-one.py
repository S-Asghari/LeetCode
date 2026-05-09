class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        processed = []
        stack = digits[:]
        while stack:
            d = stack.pop() + 1
            if 0 <= d <= 9: 
                processed.append(d)
                break
            else:
                processed.append(d-10)
                if not stack:
                    processed.append(1)
        
        processed.reverse()
        return stack + processed