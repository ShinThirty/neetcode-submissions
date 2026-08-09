# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ptrs = lists.copy()
        k = sum(1 if l else 0 for l in ptrs)
        for i, l in enumerate(ptrs):
            if l:
                heap.append((l.val, i))
        heapq.heapify(heap)

        sentinel = ListNode(-1)
        cur = sentinel

        while k > 0:
            nxt, i = heapq.heappop(heap)
            cur.next = ListNode(nxt)
            cur = cur.next
            ptrs[i] = ptrs[i].next
            if ptrs[i]:
                heapq.heappush(heap, (ptrs[i].val, i))
            else:
                k -= 1
        
        return sentinel.next
        