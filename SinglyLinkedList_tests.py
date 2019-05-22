import unittest
from ADL_SinglyLinkedList import *

class Test_SinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = ADL_SinglyLinkedList()

    def test_SinglyLinkedListInitialize(self):
        self.assertEqual(self.list.count, 0)
        self.assertTrue(self.list.isEmpty)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_SinglyLinkedListInsertOutOfBounds(self):
        with self.assertRaises(AssertionError):
            self.list.insert(1, atIndex=1)

    def test_SinglyLinkedListInsert(self):
        self.list.insert(2, atIndex=0)
        self.assertEqual(self.list.count, 1)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[0], 2)
        # self.assertTrue(selflist == [2])

        self.list.insert(0, atIndex=0)
        self.assertEqual(self.list.count, 2)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[0], 0)
        self.assertEqual(self.list[1], 2)

        listCount = self.list.count
        self.list.insert(4, atIndex=listCount)
        self.assertEqual(self.list.count, 3)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[0], 0)
        self.assertEqual(self.list[1], 2)
        self.assertEqual(self.list[2], 4)

        self.list.insert(1, atIndex=1)
        self.assertEqual(self.list.count, 4)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[0], 0)
        self.assertEqual(self.list[1], 1)
        self.assertEqual(self.list[2], 2)
        self.assertEqual(self.list[3], 4)

        self.list.insert(3, atIndex=3)
        self.assertEqual(self.list.count, 5)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[0], 0)
        self.assertEqual(self.list[1], 1)
        self.assertEqual(self.list[2], 2)
        self.assertEqual(self.list[3], 3)
        self.assertEqual(self.list[4], 4)

    def test_SinglyLinkedListAppend(self):
        start = 0
        end = 4

        for i in range(start, end+1):
            self.list.append(i)
            self.assertEqual(self.list[self.list.count-1], i)
            self.assertEqual(self.list.head, start)

    def test_SinglyLinkedListUpdate(self):
        start = 0
        end = 4

        for i in range(start, end+1):
            self.list.append(0)

        for i in range(start, end+1):
            self.list.update(i, atIndex=i)
            self.assertEqual(self.list[i], i)
            self.assertEqual(self.list.head, start)


if __name__ == '__main__':
    unittest.main()