# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def sortNodes(node1, node2):
            if node1 is None: return node2, None
            if node2 is None: return node1, None
            if node1.val <= node2.val: return node1, node2
            return node2, node1
        
        if list1 is None and list2 is None:
            return None

        list1, list2 = sortNodes(list1, list2)
        root3 = list1
        list1 = list1.next
        curNode3 = root3
        
        while list1 or list2:
            list1, list2 = sortNodes(list1, list2)
            curNode3.next = list1
            list1 = list1.next
            curNode3 = curNode3.next
        return root3