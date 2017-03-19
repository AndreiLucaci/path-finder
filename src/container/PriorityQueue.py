class PriorityQueue:
    def __init__(self):
        self.items = {}
        self.max_priority = 0

    def _enqueue_priority(self, item, priority):
        priority = self.max_priority if not priority else priority
        if priority not in self.items:
            self.items[priority] = []
        self.items[priority].insert(0, item)
        self.max_priority = self.max_priority if self.max_priority >= priority else priority
        return item

    def _dequeue_priority(self):
        if not self.items:
            return None
        item = self.items[self.max_priority].pop()
        if not self.items[self.max_priority]:
            del self.items[self.max_priority]
            self.max_priority = max(self.items.keys()) if self.items else 0
        return item

    def enqueue(self, item, priority=None):
        self._enqueue_priority(item, priority)

    def dequeue(self):
        return self._dequeue_priority()

    def size(self):
        return sum([len(self.items[i]) for i in self.items])

    def is_empty(self):
        return self.items == {}


