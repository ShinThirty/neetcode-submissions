"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}
        i = head
        dummy = Node(-1)
        j = dummy
        while i:
            cur = Node(i.val)
            j.next = cur
            j = j.next
            copy[i] = j
            i = i.next
        
        i = head
        while i:
            j = copy[i]
            j.random = copy.get(i.random, None)
            i = i.next
        
        return dummy.next
        