# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # -----------
        # Solution A
        # -----------
        # stackA = []
        # while headA:
        #     stackA.append(headA)
        #     headA = headA.next 

        # stackB = []
        # while headB:
        #     stackB.append(headB)
        #     headB = headB.next
        
        # Intersection = None
        # while stackA and stackB and stackA[-1] == stackB[-1]:
        #     Intersection = stackA.pop()
        #     stackB.pop()
        
        # return Intersection
        # -----------
        # Solution B
        # -----------
        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA:
            lenA += 1
            nodeA = nodeA.next
        while nodeB:
            lenB += 1
            nodeB = nodeB.next
        
        nodeA, nodeB = headA, headB
        
        if lenA > lenB:
            diff = lenA - lenB
            while diff:
                nodeA = nodeA.next
                diff -= 1
        elif lenB > lenA:
            diff = lenB - lenA
            while diff:
                nodeB = nodeB.next
                diff -= 1
        
        while nodeA and nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        return nodeA
