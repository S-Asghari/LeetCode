"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        newHead = Node(head.val)
        nodeMap = {None: None}
        nodeMap[head] = newHead
        if head.random not in nodeMap:
            newRandom = Node(head.random.val)
            nodeMap[head.random] = newRandom
        newHead.random = nodeMap[head.random]
        
        cur = head
        newPrev = newHead
        
        while cur.next:
            cur = cur.next
            if cur not in nodeMap:
                newCur = Node(cur.val)
                nodeMap[cur] = newCur
            newCur = nodeMap[cur]
            if cur.random not in nodeMap:
                newRandom = Node(cur.random.val)
                nodeMap[cur.random] = newRandom
            newCur.random = nodeMap[cur.random]
            newPrev.next = newCur
            newPrev = newCur
        
        return newHead
