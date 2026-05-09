# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        visited = set()
        current = head
        while current is not None:
            visited.add(current.val)
            current = current.next
        visited_list = list(visited)
        visited_list.sort() 

        cur_val = visited_list.pop()
        cur_head = ListNode(val=cur_val, next=None)
        while visited_list:
            cur_val = visited_list.pop()
            cur_head = ListNode(val=cur_val, next=cur_head)
        
        return cur_head