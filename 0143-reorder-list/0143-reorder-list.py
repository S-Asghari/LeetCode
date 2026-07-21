# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findMiddle(head):
            s, f = head, head.next # slow and fast pointers
            while (f is not None) and (f.next is not None):
                s = s.next
                f = f.next.next
            return s

        def reverseList(node, next_node):
            if node is None:
                return next_node
            prev_node, node.next = node.next, next_node
            return reverseList(prev_node, node)

        mid_node = findMiddle(head)
        last_node = reverseList(mid_node.next, None)
        mid_node.next = None

        while (head is not None) and (last_node is not None):
            next_head, next_last = head.next, last_node.next
            head.next, last_node.next = last_node, next_head
            head, last_node = next_head, next_last