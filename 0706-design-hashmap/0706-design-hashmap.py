# class MyHashMap:

#     def __init__(self):
#         self.hashmap = [[] for _ in range(2)]

#     def put(self, key: int, value: int) -> None:
#         if key in self.hashmap[0]:
#             i = self.hashmap[0].index(key)
#             self.hashmap[1][i] = value
#         else:
#             self.hashmap[0].append(key)
#             self.hashmap[1].append(value)

#     def get(self, key: int) -> int:
#         if key in self.hashmap[0]:
#             i = self.hashmap[0].index(key)
#             return self.hashmap[1][i]
#         else:
#             return -1
        
#     def remove(self, key: int) -> None:
#         if key in self.hashmap[0]:
#             i = self.hashmap[0].index(key)
#             del self.hashmap[0][i]
#             del self.hashmap[1][i]

# NeetCode's Solution
class ListNode():
    def __init__(self, k = -1, v = -1, next = None):
        self.key = k
        self.value = v
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode() for _ in range(10000)]

    def hash(self, key: int) -> int:
        return key % len(self.hashmap)
    
    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        curNode = self.hashmap[idx]
        while curNode.next:
            if curNode.next.key == key:
                curNode.next.value = value
                return
            curNode = curNode.next
        curNode.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = self.hash(key)
        curNode = self.hashmap[idx].next
        while curNode:
            if curNode.key == key:
                return curNode.value
            curNode = curNode.next
        return -1
        
    def remove(self, key: int) -> None:
        idx = self.hash(key)
        curNode = self.hashmap[idx]
        while curNode and curNode.next:
            if curNode.next.key == key:
                curNode.next = curNode.next.next
                return
            curNode = curNode.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)