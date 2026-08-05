class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        
        n = self.keys[key]
        self._delete_(n)
        self._prepend_(n)
        return n.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            if len(self.keys) == self.capacity:
                evict = self.tail.prev
                self._delete_(evict)
                del self.keys[evict.key]
            n = ListNode(key, value)
            self._prepend_(n)
            self.keys[key] = n
        else:
            n = self.keys[key]
            n.val = value
            self._delete_(n)
            self._prepend_(n)

    
    def _prepend_(self, n):
        n.next = self.head.next
        n.prev = self.head
        n.next.prev = n
        n.prev.next = n
    
    def _delete_(self, n):
        n.next.prev = n.prev
        n.prev.next = n.next
