# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        leftNode = ListNode(-101) # dummy node
        leftNode.next, rightNode = head, head
        c = 0 # occurance count
        while rightNode:
            if rightNode.val == leftNode.next.val:
                c += 1
                rightNode = rightNode.next
                continue
            if c > 1:
                leftNode.next.val = rightNode.val
            elif c == 1:
                leftNode.next.next.val = rightNode.val
                leftNode = leftNode.next
            c = 1
            rightNode = rightNode.next
        
        if c > 1:
            leftNode.next = None
        elif c == 1:
            leftNode.next.next = None
            leftNode = leftNode.next
        
        return head if leftNode.val >= -100 else None