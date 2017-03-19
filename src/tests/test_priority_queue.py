from unittest import TestCase

from src.container.PriorityQueue import PriorityQueue

class TestPriorityQueue(TestCase):
    def create_sut(self):
        return PriorityQueue()

    def test_enqueue_item_is_added(self):
        sut = self.create_sut()
        sut.enqueue(1)
        self.assertEqual(1, sut.size())

    def test_enqueue_item_with_priority_is_added(self):
        sut = self.create_sut()
        sut.enqueue(1, 1)
        self.assertEqual(1, sut.max_priority())
        self.assertEqual(1, sut.size())

    def test_dequeue_by_priority(self):
        sut = self.create_sut()
        sut.enqueue(1)
        sut.enqueue(2, 3)
        sut.enqueue(3, 3)

        self.assertEqual(2, sut.peek())
        self.assertEqual(3, sut.max_priority())

    def test_dequeue_max_priotity_changes(self):
        sut = self.create_sut()
        sut.enqueue(1)
        sut.enqueue(2, 2)
        sut.enqueue(3, 3)

        self.assertEqual(3, sut.max_priority())
        self.assertEqual(3, sut.dequeue())
        self.assertEqual(2, sut.max_priority())

    def test_dequeue_single_element_the_queue_remains_empty(self):
        sut = self.create_sut()
        sut.enqueue(1)

        self.assertEqual(1, sut.dequeue())
        self.assertTrue(sut.is_empty())

    def test_is_empty(self):
        sut = self.create_sut()
        self.assertTrue(sut.is_empty())
