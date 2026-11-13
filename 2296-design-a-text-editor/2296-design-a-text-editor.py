# class TextEditor:

#     def __init__(self):
#         self.content = []
#         self.cursor = 0

#     def addText(self, text: str) -> None:
#         self.content = self.content[: self.cursor] + list(text) + self.content[self.cursor: ]
#         self.cursor += len(text)

#     def deleteText(self, k: int) -> int:
#         k = min(k, self.cursor)
#         self.content = self.content[: self.cursor - k] + self.content[self.cursor: ]
#         self.cursor -= k
#         return k

#     def cursorLeft(self, k: int) -> str:
#         k = min(k, self.cursor)
#         self.cursor -= k
#         return "".join(self.content[self.cursor - min(10, self.cursor): self.cursor])

#     def cursorRight(self, k: int) -> str:
#         k = min(k, len(self.content) - self.cursor)
#         self.cursor += k
#         return "".join(self.content[self.cursor - min(10, self.cursor): self.cursor])

# -------------------
# TIME LIMIT EXCEEDED
# -------------------

class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)

    def deleteText(self, k: int) -> int:
        removed = 0
        for _ in range(min(k, len(self.left))):
            self.left.pop()
            removed += 1
        return removed

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.left))):
            self.right.append(self.left.pop())
        
        return "".join(self.left[-min(10, len(self.left)):])
        
    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.right))):
            self.left.append(self.right.pop())
        
        return "".join(self.left[-min(10, len(self.left)):])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)