class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures.reverse()
        n = len(temperatures)
        results = [0 for i in range(n)]
        stack = []
        for i in range(n):
            if not stack:
                stack.append((temperatures[i], 0))
            else:
                if stack[-1][0] > temperatures[i]:
                    results[i] = 1
                    stack.append((temperatures[i], 0))
                else:
                    removed = 0
                    while stack and stack[-1][0] <= temperatures[i]:
                        removedItem = stack.pop()
                        removed += removedItem[1] + 1
                    if stack:
                        results[i] = removed + 1
                    stack.append((temperatures[i], removed))
                
        results.reverse()
        return results