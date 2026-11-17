# --------------
# First Solution
# --------------
# from collections import deque

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.lru = deque()
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.lru.remove(key)
#             self.lru.append(key)
#             return self.cache[key]
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.lru.remove(key)
#         elif len(self.lru) == self.capacity:
#             removedKey = self.lru.popleft()
#             del self.cache[removedKey]
#         self.lru.append(key)
#         self.cache[key] = value

class Node:

    def __init__(self, key: int = -1, val: int = -1) -> None:
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node: Node) -> None:
        prv, nxt = self.tail.prev, self.tail
        node.prev, node.next = prv, nxt
        prv.next, nxt.prev = node, node

    def remove(self, node: Node) -> None:
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        else: 
            if len(self.cache) == self.cap:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]
            node = Node(key=key, val=value)
            self.cache[key] = node
        self.insert(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)