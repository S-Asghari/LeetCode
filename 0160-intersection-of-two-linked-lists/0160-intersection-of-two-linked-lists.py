# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = []
        while headA:
            stackA.append(headA)
            headA = headA.next 

        stackB = []
        while headB:
            stackB.append(headB)
            headB = headB.next
        
        Intersection = None
        while stackA and stackB and stackA[-1] == stackB[-1]:
            Intersection = stackA.pop()
            stackB.pop()
        
        return Intersection