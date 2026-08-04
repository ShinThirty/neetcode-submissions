# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        p = head.next
        head.next = None
        while p is not None:
            q = p.next
            p.next = head
            head = p
            p = q
        
        return head