# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        node = root
        r = 0

        while l1 or l2:
            node.next = ListNode()
            node = node.next

            total = 0
            if l1:
                total += l1.val
            if l2:
                total += l2.val
            total += r

            if total >= 10:
                r = total // 10
                total %= 10
            else:
                r = 0

            node.val = total
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if r > 0:
            node.next = ListNode(val=r)

        return root.next