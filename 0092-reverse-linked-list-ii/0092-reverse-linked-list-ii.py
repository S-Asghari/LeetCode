# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # NeetCode's solution
        dummy = ListNode(0, head)
        
        leftPrev, cur = dummy, head
        for _ in range(1, left):
            leftPrev, cur = cur, cur.next
        
        # Now: cur = "left", leftPrev = "node before left"
        prev = None
        for _ in range(left, right+1):
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp

        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next