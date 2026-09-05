from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.lru = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.lru.remove(key)
        elif len(self.lru) == self.capacity:
            removedKey = self.lru.popleft()
            del self.cache[removedKey]
        self.lru.append(key)
        self.cache[key] = value
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)