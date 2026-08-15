class MinStack:

    def __init__(self):
        self.stack = [] # [(v1, min so far), (v2, min so far), ...]

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value, value))
        else:
            prevMin = self.getMin()
            self.stack.append((value, min(value, prevMin)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()