# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(-1, head)
        prev, cur, nxt = None, head, head.next # n >= 1
        cse, pse = head, sentinel
        seq = 0
        while cur:
            prev = None
            for _ in range(k):
                cur.next = prev
                prev = cur
                cur = nxt
                seq = (seq + 1) % k
                if not cur:
                    break
                nxt = cur.next

            pse.next = prev
            if cur:
                pse = cse
                cse = cur
        
        if seq > 0:
            cur = prev
            prev = None
            nxt = cur.next
            while cur:
                cur.next = prev
                prev = cur
                cur = nxt
                if cur:
                    nxt = cur.next
            pse.next = prev
        
        return sentinel.next