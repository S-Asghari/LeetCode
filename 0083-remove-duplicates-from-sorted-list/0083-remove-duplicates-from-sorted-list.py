# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        leftNode, rightNode = head, head
        while rightNode:
            if rightNode.val == leftNode.val:
                rightNode = rightNode.next
                continue
            leftNode.next.val = rightNode.val
            leftNode = leftNode.next
            rightNode = rightNode.next
        
        if leftNode: 
            leftNode.next = None
        return head