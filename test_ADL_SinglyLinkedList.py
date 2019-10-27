import unittest
from ADL_SinglyLinkedList import *

class Test_SinglyLinkedListNode(unittest.TestCase):

    def test_SinglyLinkedListNodeInitialize(self):
        with self.assertRaises(TypeError):
            aList = ADL_SinglyLinkedListNode()

class Test_SinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = ADL_SinglyLinkedList()

    def tearDown(self):
        self.list = None

    def test_SinglyLinkedListInitialize(self):
        self.assertEqual(len(self.list), 0)
        self.assertTrue(self.list.isEmpty)

    def test_SinglyLinkedListGetValueOutOfBounds(self):
        with self.assertRaises(AssertionError):
            self.list.getValueAtIndex(0)
        with self.assertRaises(AssertionError):
            self.list.getValueAtIndex(1)

    def test_SinglyLinkedListInsertOutOfBounds(self):
        with self.assertRaises(AssertionError):
            self.list.insertValueAtIndex(1, 1)

    def test_SinglyLinkedListInsert(self):
        self.list.insertValueAtIndex(2, 0)
        self.assertEqual(len(self.list), 1)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[0], 2)
        self.assertTrue(self.list == [2])
        self.assertEqual(self.list, [2])

        self.list.insertValueAtIndex(0, 0)
        self.assertEqual(len(self.list), 2)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[0], 0)
        self.assertTrue(self.list == [0, 2])
        self.assertEqual(self.list, [0, 2])

        listLen = len(self.list)
        self.list.insertValueAtIndex(4, listLen)
        self.assertEqual(len(self.list), 3)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[listLen], 4)
        self.assertTrue(self.list == [0, 2, 4])
        self.assertEqual(self.list, [0, 2, 4])

        self.list.insertValueAtIndex(1, 1)
        self.assertEqual(len(self.list), 4)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[1], 1)
        self.assertTrue(self.list == [0, 1, 2, 4])
        self.assertEqual(self.list, [0, 1, 2, 4])

        self.list.insertValueAtIndex(3, 3)
        self.assertEqual(len(self.list), 5)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[3], 3)
        self.assertTrue(self.list == [0, 1, 2, 3, 4])
        self.assertEqual(self.list, [0, 1, 2, 3, 4])

    def test_SinglyLinkedListAppend(self):
        start = 0
        end = 4

        for i in range(start, end+1):
            self.list.appendValue(i)
            self.assertEqual(self.list[len(self.list)-1], i)
            self.assertEqual(self.list[0], start)

    def test_SinglyLinkedListUpdate(self):
        start = 0
        end = 4

        for i in range(start, end+1):
            self.list.appendValue(i)

        self.list[0] = 10
        self.assertEqual(len(self.list), 5)
        self.assertEqual(self.list, [10, 1, 2, 3, 4])
        self.assertEqual(self.list[0], 10)

        self.list.updateValueAtIndex(12, 2)
        self.assertEqual(len(self.list), 5)
        self.assertEqual(self.list, [10, 1, 12, 3, 4])
        self.assertEqual(self.list[0], 10)
        self.assertEqual(self.list[2], 12)

        self.list[4] = 14
        self.assertEqual(len(self.list), 5)
        self.assertEqual(self.list, [10, 1, 12, 3, 14])
        self.assertEqual(self.list[0], 10)
        self.assertEqual(self.list[4], 14)

    def test_SinglyLinkedListRemoveOutOfBounds(self):
        with self.assertRaises(AssertionError):
            self.list.removeValueAtIndex(1)

    def test_SinglyLinkedListRemove(self):
        for i in range(0, 4+1):
            self.list.appendValue(i)

        self.assertTrue(self.list == [0,1,2,3,4])

        self.assertEqual(self.list.removeValueAtIndex(3), 3)
        self.assertFalse(self.list.isEmpty)
        self.assertTrue(self.list == [0,1,2,4])
        self.assertEqual(len(self.list), 4)
        self.assertEqual(self.list[0], 0)
        self.assertEqual(self.list[len(self.list)-1], 4)

        self.assertEqual(self.list.removeValueAtIndex(1), 1)
        self.assertFalse(self.list.isEmpty)
        self.assertTrue(self.list == [0,2,4])
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list[0], 0)
        self.assertEqual(self.list[len(self.list)-1], 4)

        self.assertEqual(self.list.removeValueAtIndex(len(self.list)-1), 4)
        self.assertFalse(self.list.isEmpty)
        self.assertTrue(self.list == [0,2])
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list[0], 0)
        self.assertEqual(self.list[len(self.list)-1], 2)

        self.assertEqual(self.list.removeValueAtIndex(0), 0)
        self.assertFalse(self.list.isEmpty)
        self.assertTrue(self.list == [2])
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list[0], 2)
        self.assertEqual(self.list[len(self.list)-1], 2)

        self.assertEqual(self.list.removeValueAtIndex(0), 2)
        self.assertTrue(self.list.isEmpty)
        self.assertTrue(self.list == [])
        self.assertEqual(len(self.list), 0)


    def test_SinglyLinkedListIterator(self):
        for i in range(5):
            self.list.appendValue(i)

        for k,v in enumerate(self.list):
            self.assertEqual(k, v)


if __name__ == '__main__':
    unittest.main()