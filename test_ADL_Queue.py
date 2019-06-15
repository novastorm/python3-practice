import unittest
from ADL_Queue import *

def test_base(base_cls):
    class BaseClassSkipper(base_cls):
        @classmethod
        def setUpClass(cls):
            if cls is BaseClassSkipper:
                raise unittest.SkipTest("Base class")
            super().setUpClass()
    return BaseClassSkipper

@test_base
class Base_ADL_Queue_tests(unittest.TestCase):

    def setUp(self):
        raise NotImplementedError

    def test_queue_initialization(self):
        self.assertTrue(self.queue.isEmpty)
        self.assertEqual(self.queue.count, 0)
        self.assertIsNone(self.queue.peek)


    def test_queue_enqueue(self):
        self.queue.enqueue(0)
        self.assertFalse(self.queue.isEmpty)
        self.assertEqual(self.queue.count, 1)
        self.assertEqual(self.queue.peek, 0)
        self.assertEqual(self.queue, [0])

        self.queue.enqueue(1)
        self.assertFalse(self.queue.isEmpty)
        self.assertEqual(self.queue.count, 2)
        self.assertEqual(self.queue.peek, 0)
        self.assertEqual(self.queue, [0, 1])

        self.queue.enqueue(2)
        self.assertFalse(self.queue.isEmpty)
        self.assertEqual(self.queue.count, 3)
        self.assertEqual(self.queue.peek, 0)
        self.assertEqual(self.queue, [0, 1, 2])


    def test_queue_dequeue(self):
        self.assertIsNone(self.queue.dequeue())
        for i in range(3):
            self.queue.enqueue(i)

        self.assertEqual(self.queue.peek, 0)
        self.assertEqual(self.queue.dequeue(), 0)
        self.assertEqual(self.queue.count, 2)

        self.assertEqual(self.queue.peek, 1)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.count, 1)

        self.assertEqual(self.queue.peek, 2)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.count, 0)

        self.assertIsNone(self.queue.peek)



class test_ADL_SinglyLinkedList_Queue(Base_ADL_Queue_tests):

    def setUp(self):
        self.queue = ADL_SinglyLinkedList_Queue()


class test_ADL_DoublyLinkedList_Queue(Base_ADL_Queue_tests):

    def setUp(self):
        self.queue = ADL_DoublyLinkedList_Queue()


class test_ADL_List_Queue(Base_ADL_Queue_tests):

    def setUp(self):
        self.queue = ADL_List_Queue()


if __name__ == '__main__':
    unittest.main()