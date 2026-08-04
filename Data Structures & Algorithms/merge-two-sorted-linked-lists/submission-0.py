# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2

        dummy = ListNode(-1)
        cur = dummy
        while i is not None and j is not None:
            if i.val <= j.val:
                cur.next = i
                i = i.next
            else:
                cur.next = j
                j = j.next
            cur = cur.next
        
        if i is not None:
            cur.next = i
        else:
            cur.next = j
        
        return dummy.next
        