class MyQueue:
    def __init__(self):
        self.stack = []
        self.helper_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            top = self.stack.pop()
            self.helper_stack.append(top)
        
        output = self.helper_stack.pop()
        
        while self.helper_stack:
            top = self.helper_stack.pop()
            self.stack.append(top)

        return output

    def peek(self) -> int:
        while self.stack:
            top = self.stack.pop()
            self.helper_stack.append(top)
        
        output = self.helper_stack[-1]
        
        while self.helper_stack:
            top = self.helper_stack.pop()
            self.stack.append(top)

        return output

    def empty(self) -> bool:
        if not self.stack:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()