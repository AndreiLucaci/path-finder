from itertools import chain

class PriorityQueue:
    def __init__(self):
        self._items = {}
        self._max_priority = 0

    def _enqueue_priority(self, item, priority):
        priority = self._max_priority if not priority else priority
        if priority not in self._items:
            self._items[priority] = []
        self._items[priority].insert(0, item)
        self._max_priority = self._max_priority if self._max_priority >= priority else priority
        return item

    def _dequeue_priority(self, is_peek=False):
        if not self._items:
            return None

        if is_peek:
            return self._items[self._max_priority][-1]

        item = self._items[self._max_priority].pop()
        if not self._items[self._max_priority]:
            del self._items[self._max_priority]
            self._max_priority = max(self._items.keys()) if self._items else 0
        return item

    def enqueue(self, item, priority=None):
        self._enqueue_priority(item, priority)

    def dequeue(self):
        return self._dequeue_priority()

    def size(self):
        return sum([len(self._items[i]) for i in self._items])

    def is_empty(self):
        return self._items == {}

    def max_priority(self):
        return self._max_priority

    def peak_all_items(self):
        return chain(self._items[i] for i in self._items)

    def peek(self):
        return self._dequeue_priority(True)

