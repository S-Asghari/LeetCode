"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None

        def helper(cur: 'Node') -> 'Node':
            tail = cur
            while cur is not None:
                next_node = cur.next
                if cur.child is not None:
                    child_head = cur.child
                    child_tail = helper(child_head)

                    cur.next = child_head
                    child_head.prev = cur
                    cur.child = None

                    child_tail.next = next_node
                    if next_node is not None:
                        next_node.prev = child_tail
                    tail = child_tail

                cur = next_node
                if cur is not None:
                    tail = cur

            return tail


        helper(head)
        return head