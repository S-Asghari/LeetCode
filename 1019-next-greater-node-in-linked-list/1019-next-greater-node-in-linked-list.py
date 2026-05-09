# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # 1. For each node, traverse the linked list until you find a greater value
        # 2. For the next node, if its value is lower, you don't need to traverse the list again. You already have the answer.
        answer = []
        
        prev = head.val
        curr = head.val
        idx = 0
        temporary_list = [(curr, idx)]
        
        while head.next:
            # print(temporary_list)
            head = head.next
            idx += 1
            curr = head.val
            
            if curr > prev:
                new_tempo = []
                for node, i in temporary_list:
                    if node < curr:
                        answer.append((curr, i))
                    else:
                        new_tempo.append((node, i))
                temporary_list = new_tempo
            
            temporary_list.append((curr, idx))
            prev = curr

        for node, i in temporary_list:
            answer.append((0, i))

        answer = sorted(answer, key = lambda x: x[1])
        answer = [a[0] for a in answer]
                
        return answer