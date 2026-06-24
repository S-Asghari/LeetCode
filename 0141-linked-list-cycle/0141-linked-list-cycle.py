# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        visited = set()
        cur = head
        visited.add(cur)
        while cur.next:
            if cur.next not in visited:
                cur = cur.next
                visited.add(cur)
            else:
                return True
        return False