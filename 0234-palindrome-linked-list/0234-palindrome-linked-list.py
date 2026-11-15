# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
    # -------------------------------------------
    # O(n) Space Complexity, O(n) Time Complexity
    # -------------------------------------------
    #     count = 0
    #     cur = head
    #     while cur:
    #         count += 1
    #         cur = cur.next
        
    #     if count == 1:
    #         return True

    #     def checkOnePair(i, leftNode):
    #         if i == count // 2:
    #             if count % 2 == 0: rightNode = leftNode.next
    #             else: rightNode = leftNode.next.next
    #             if leftNode.val == rightNode.val: return True, rightNode.next 
    #             else: return False, rightNode.next

    #         if i < count // 2:
    #             checkInnerPairs, rightNode = checkOnePair(i + 1, leftNode.next)
    #             if not checkInnerPairs or leftNode.val != rightNode.val:
    #                 return False, rightNode.next
    #             else:
    #                 return True, rightNode.next
        
    #     isPal, _ = checkOnePair(1, head)
    #     return isPal
    
    # -------------------------------------------
    # O(n) Space Complexity, O(n) Time Complexity
    # -------------------------------------------
        nums = []

        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True