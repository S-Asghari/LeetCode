# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # insertion sort
        # n = len(nums)
        # for j in range(1, n):
        #     key = nums[j]
        #     i = j-1
        #     while i >= 0 and nums[i] > key:
        #         nums[i+1] = nums[i]
        #         i -= 1
        #     nums[i+1] = key
        j = head
        while j:
            key = j.val
            i = j.next
            while i:
                if i.val < key:
                    i.val, key = key, i.val
                i = i.next
            j.val = key
            j = j.next
        
        return head