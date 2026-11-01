class MyHashMap:

    def __init__(self):
        self.hashmap = [[] for _ in range(2)]

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap[0]:
            i = self.hashmap[0].index(key)
            self.hashmap[1][i] = value
        else:
            self.hashmap[0].append(key)
            self.hashmap[1].append(value)

    def get(self, key: int) -> int:
        if key in self.hashmap[0]:
            i = self.hashmap[0].index(key)
            return self.hashmap[1][i]
        else:
            return -1
        
    def remove(self, key: int) -> None:
        if key in self.hashmap[0]:
            i = self.hashmap[0].index(key)
            del self.hashmap[0][i]
            del self.hashmap[1][i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)