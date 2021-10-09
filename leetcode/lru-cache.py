class Node:
    def __init__(self, key, val, node, prev):
        self.key = key
        self.val = val
        self.next = node
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, None, self.head)
        self.head.next = self.tail
        self.size = capacity
        self.d = {}

    def get(self, key: int) -> int:
        if key in self.d:
            self.d[key].prev.next = self.d[key].next
            self.d[key].next.prev = self.d[key].prev

            self.d[key].next = self.head.next
            self.d[key].prev = self.head

            self.head.next.prev = self.d[key]
            self.head.next = self.d[key]

            return self.d[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value
            self.get(key)
        else:
            if self.size == len(self.d):
                del self.d[self.tail.prev.key]
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

            newNode = Node(key, value, self.head.next, self.head)
            self.head.next.prev = newNode
            self.head.next = newNode
            self.d[key] = newNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
