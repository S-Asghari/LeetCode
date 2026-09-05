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

# ------------------------------------
# Second Solution: NeetCode's Solution
# ------------------------------------
class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = self.right = Node(-1, -1)
        self.left.next , self.right.prev = self.right, self.left

    def remove(self, node: int) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev 

    def insert(self, node: int) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) == self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)