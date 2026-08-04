# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        i = l1
        j = l2
        k = dummy

        while i or j or carry > 0:
            vi = 0
            if i:
                vi = i.val
                i = i.next
            vj = 0
            if j:
                vj = j.val
                j = j.next
            carry, v = divmod(vi + vj + carry, 10)
            k.next = ListNode(v, None)
            k = k.next
        
        return dummy.next