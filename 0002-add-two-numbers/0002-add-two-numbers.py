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

            summ = 0
            if l1:
                summ += l1.val
            if l2:
                summ += l2.val
            summ += r

            if summ >= 10:
                r = summ // 10
                summ %= 10
            else:
                r = 0

            print(f"summ: {summ}, r: {r}")
            node.val = summ
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if r > 0:
            print(f"yes, r is {r}.")
            node.next = ListNode()
            node = node.next
            node.val = r

        return root.next