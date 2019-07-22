import unittest
from ADL_SinglyLinkedList import *

class Test_SinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = ADL_SinglyLinkedList()

    def teardown(self):
        self.list = None

    def test_SinglyLinkedListInitialize(self):
        self.assertEqual(len(self.list), 0)
        self.assertTrue(self.list.isEmpty)

    def test_SinglyLinkedListGetValueOutOfBounds(self):
        with self.assertRaises(AssertionError):
            self.list.getValue(atIndex=0)
        with self.assertRaises(AssertionError):
            self.list.getValue(atIndex=1)

    def test_SinglyLinkedListInsertOutOfBounds(self):
        with self.assertRaises(AssertionError):
            self.list.insertValue(1, atIndex=1)

    def test_SinglyLinkedListInsert(self):
        self.list.insertValue(2, atIndex=0)
        self.assertEqual(len(self.list), 1)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[0], 2)
        self.assertTrue(self.list == [2])
        self.assertEqual(self.list, [2])

        self.list.insertValue(0, atIndex=0)
        self.assertEqual(len(self.list), 2)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[0], 0)
        self.assertTrue(self.list == [0, 2])
        self.assertEqual(self.list, [0, 2])

        listLen = len(self.list)
        self.list.insertValue(4, atIndex=listLen)
        self.assertEqual(len(self.list), 3)        
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[listLen], 4)
        self.assertTrue(self.list == [0, 2, 4])
        self.assertEqual(self.list, [0, 2, 4])

        self.list.insertValue(1, atIndex=1)
        self.assertEqual(len(self.list), 4)
        self.assertFalse(self.list.isEmpty)
        self.assertEqual(self.list[1], 1)
        self.assertTrue(self.list == [0, 1, 2, 4])
        self.assertEqual(self.list, [0, 1, 2, 4])

        self.list.insertValue(3, atIndex=3)
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

        self.list.updateValue(12, 2)
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
            self.list.removeValue(atIndex=1)

    def test_SinglyLinkedListRemove(self):
        for i in range(0, 4+1):
            self.list.appendValue(i)

        self.assertTrue(self.list == [0,1,2,3,4])

        self.assertEqual(self.list.removeValue(atIndex=3), 3)
        self.assertFalse(self.list.isEmpty)
        self.assertTrue(self.list == [0,1,2,4])
        self.assertEqual(len(self.list), 4)
        self.assertEqual(self.list[0], 0)
        self.assertEqual(self.list[len(self.list)-1], 4)

        self.assertEqual(self.list.removeValue(atIndex=1), 1)
        self.assertFalse(self.list.isEmpty)
        self.assertTrue(self.list == [0,2,4])
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list[0], 0)
        self.assertEqual(self.list[len(self.list)-1], 4)

        self.assertEqual(self.list.removeValue(atIndex=len(self.list)-1), 4)
        self.assertFalse(self.list.isEmpty)
        self.assertTrue(self.list == [0,2])
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list[0], 0)
        self.assertEqual(self.list[len(self.list)-1], 2)

        self.assertEqual(self.list.removeValue(atIndex=0), 0)
        self.assertFalse(self.list.isEmpty)
        self.assertTrue(self.list == [2])
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list[0], 2)
        self.assertEqual(self.list[len(self.list)-1], 2)

        self.assertEqual(self.list.removeValue(atIndex=0), 2)
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