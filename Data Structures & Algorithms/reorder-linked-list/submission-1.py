# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        i = head
        j = slow.next
        slow.next = None

        if j is None:
            return

        prev = j
        cur = j.next
        prev.next = None
        while cur is not None:
            prev = cur
            cur = cur.next
            prev.next = j
            j = prev
        
        ip = i
        jp = j
        while ip is not None and jp is not None:
            ti = ip.next
            ip.next = jp
            tj = jp.next
            jp.next = ti
            ip = ti
            jp = tj

