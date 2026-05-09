class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [(index, height)]
        max_area = 0
        for i in range(len(heights)):
            if not stack:
                stack.append((i, heights[i]))
            else:
                if stack[-1][1] < heights[i]:
                    stack.append((i, heights[i]))
                else:
                    last_index = i
                    while stack and stack[-1][1] >= heights[i]:
                        last_index, last_height = stack.pop()
                        max_area = max(
                            max_area, 
                            last_height*(i - last_index)
                            )
                    stack.append((last_index, heights[i]))
  
        final_index = len(heights)
        while stack:
            index, height = stack.pop()
            max_area = max(
                            max_area, 
                            height*(final_index - index)
                            )

        return max_area