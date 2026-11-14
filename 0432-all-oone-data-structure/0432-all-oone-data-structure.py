class CountNode:
    def __init__(self, count: int):
        self.count = count
        self.left = None
        self.right = None
        self.keys = set()


class AllOne:
    def __init__(self):
        self.head = CountNode(0)
        self.tail = CountNode(0)
        self.head.right = self.tail
        self.tail.left = self.head
        self.keyNode = {}

    def inc(self, key: str) -> None:
        if key not in self.keyNode:
            node = self.head.right
            if node is self.tail or node.count != 1:
                new_node = CountNode(1)
                new_node.left = self.head
                new_node.right = node
                self.head.right = new_node
                node.left = new_node
                node = new_node
        else:
            current = self.keyNode[key]
            node = current.right
            if node is self.tail or node.count != current.count + 1:
                new_node = CountNode(current.count + 1)
                new_node.left = current
                new_node.right = node
                current.right = new_node
                node.left = new_node
                node = new_node
            current.keys.remove(key)
            if not current.keys:
                current.left.right = current.right
                current.right.left = current.left

        node.keys.add(key)
        self.keyNode[key] = node

    def dec(self, key: str) -> None:
        current = self.keyNode[key]
        if current.count == 1:
            del self.keyNode[key]
        else:
            node = current.left
            if node is self.head or node.count != current.count - 1:
                new_node = CountNode(current.count - 1)
                new_node.left = node
                new_node.right = current
                node.right = new_node
                current.left = new_node
                node = new_node
            node.keys.add(key)
            self.keyNode[key] = node

        current.keys.remove(key)
        if not current.keys:
            current.left.right = current.right
            current.right.left = current.left

    def getMaxKey(self) -> str:
        if self.tail.left is self.head:
            return ""
        return next(iter(self.tail.left.keys))

    def getMinKey(self) -> str:
        if self.head.right is self.tail:
            return ""
        return next(iter(self.head.right.keys))
