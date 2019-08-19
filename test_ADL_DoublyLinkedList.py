import unittest
from ADL_DoublyLinkedList import *

class Test_DoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = ADL_DoublyLinkedList()

    def test_DoublyLinkedListInitialize(self):
        self.assertEqual(self.list.count, 0)
        self.assertTrue(self.list.isEmpty)
        self.assertIsNone(self.list.first)
        self.assertIsNone(self.list.last)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_DoublyLinkedListGetValueOutOfBounds(self):
        with self.assertRaises(AssertionError):
            self.list.getValue(atIndex=0)
        with self.assertRaises(AssertionError):
            self.list.getValue(atIndex=1)
        with self.assertRaises(AssertionError):
            self.list[0]
        with self.assertRaises(AssertionError):
            self.list[1]

    def test_DoublyLinkedListInsertOutOfBounds(self):
        with self.assertRaises(AssertionError):
            self.list.insert(1, atIndex=1)

    def test_DoublyLinkedListInsert(self):
        self.list.insert(2, atIndex=0)
        self.assertEqual(self.list.count, 1)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list.first, 2)
        self.assertEqual(self.list.last, 2)
        self.assertEqual(self.list[0], 2)
        self.assertTrue(self.list == [2])
        self.assertEqual(self.list, [2])

        self.list.insert(0, atIndex=0)
        self.assertEqual(self.list.count, 2)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list.first, 0)
        self.assertEqual(self.list.last, 2)
        self.assertEqual(self.list[0], 0)
        self.assertTrue(self.list == [0, 2])

        listCount = self.list.count
        self.list.insert(4, atIndex=listCount)
        self.assertEqual(self.list.count, 3)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list.first, 0)
        self.assertEqual(self.list.last, 4)
        self.assertEqual(self.list[listCount], 4)
        self.assertTrue(self.list == [0, 2, 4])

        self.list.insert(1, atIndex=1)
        self.assertEqual(self.list.count, 4)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list.first, 0)
        self.assertEqual(self.list.last, 4)
        self.assertEqual(self.list[1], 1)
        self.assertTrue(self.list == [0, 1, 2, 4])

        self.list.insert(3, atIndex=3)
        self.assertEqual(self.list.count, 5)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list.first, 0)
        self.assertEqual(self.list.last, 4)
        self.assertEqual(self.list[3], 3)
        self.assertTrue(self.list == [0, 1, 2, 3, 4])

    def test_DoublyLinkedListAppend(self):
        start = 0
        end = 4

        for i in range(start, end+1):
            self.list.append(i)
            self.assertEqual(self.list[self.list.count-1], i)
            self.assertEqual(self.list.first, start)
            self.assertEqual(self.list.last, i)

    def test_DoublyLinkedListUpdate(self):
        start = 0
        end = 4

        for i in range(start, end+1):
            self.list.append(0)

        self.assertTrue(self.list == [0, 0, 0, 0, 0])

        for i in range(start, end+1):
            self.list[i] = i
            self.assertEqual(self.list[i], i)
            self.assertEqual(self.list.head, start)

        self.assertTrue(self.list == [0, 1, 2, 3, 4])


    def test_DoublyLinkedListRemoveOutOfBounds(self):
        with self.assertRaises(AssertionError):
            self.list.remove(atIndex=1)

    def test_DoublyLinkedListRemove(self):
        for i in range(0, 4+1):
            self.list.append(i)

        self.assertTrue(self.list == [0,1,2,3,4])

        self.assertEqual(self.list.remove(atIndex=3), 3)
        self.assertTrue(self.list == [0,1,2,4])
        self.assertEqual(self.list.count, 4)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list.first, 0)
        self.assertEqual(self.list.last, 4)
        self.assertEqual(self.list.head, 0)
        self.assertEqual(self.list[self.list.count-1], 4)

        self.assertEqual(self.list.remove(atIndex=1), 1)
        self.assertTrue(self.list == [0,2,4])
        self.assertEqual(self.list.count, 3)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list.first, 0)
        self.assertEqual(self.list.last, 4)
        self.assertEqual(self.list.head, 0)
        self.assertEqual(self.list[self.list.count-1], 4)

        self.assertEqual(self.list.remove(atIndex=self.list.count-1), 4)
        self.assertEqual(self.list.count, 2)
        self.assertTrue(self.list == [0,2])
        self.assertEqual(self.list.first, 0)
        self.assertEqual(self.list.last, 2)
        self.assertEqual(self.list.head, 0)
        self.assertEqual(self.list[self.list.count-1], 2)

        self.assertEqual(self.list.remove(atIndex=0), 0)
        self.assertTrue(self.list == [2])
        self.assertEqual(self.list.count, 1)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list.first, 2)
        self.assertEqual(self.list.last, 2)
        self.assertEqual(self.list.head, 2)
        self.assertEqual(self.list[self.list.count-1], 2)

        self.assertEqual(self.list.remove(atIndex=0), 2)
        self.assertTrue(self.list == [])
        self.assertEqual(self.list.count, 0)
        self.assertTrue(self.list.isEmpty)
        self.assertIsNone(self.list.first)
        self.assertIsNone(self.list.last)
        self.assertIsNone(self.list.head)


    def test_DoublyLinkedListIterator(self):
        for i in range(5):
            self.list.append(i)

        for k,v in enumerate(self.list):
            self.assertEqual(k, v)


if __name__ == '__main__':
    unittest.main()
