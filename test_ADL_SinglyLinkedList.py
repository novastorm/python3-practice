import unittest
from ADL_SinglyLinkedList import *

class Test_SinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = None

    def teardown(self):
        self.list = None

    def test_SinglyLinkedListInitialize(self):
        self.assertEqual(ADL_SinglyLinkedList.len(self.list), 0)
        self.assertTrue(ADL_SinglyLinkedList.isEmpty(self.list))

    def test_SinglyLinkedListString(self):
        node0 = ADL_SinglyLinkedList(0)
        node1 = ADL_SinglyLinkedList(1)
        node2 = ADL_SinglyLinkedList(2)
        node3 = ADL_SinglyLinkedList(3)
        node4 = ADL_SinglyLinkedList(4)
        node0.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4

        self.assertEqual(str(node0), '[0, 1, 2, 3, 4]')

    def test_SinglyLinkedListGetValueOutOfBounds(self):
        with self.assertRaises(AssertionError):
            ADL_SinglyLinkedList.getNode(self.list, atIndex=0)
        with self.assertRaises(AssertionError):
            ADL_SinglyLinkedList.getNode(self.list, atIndex=1)

    def test_SinglyLinkedListInsertOutOfBounds(self):
        newNode = ADL_SinglyLinkedList(1)
        with self.assertRaises(AssertionError):
            ADL_SinglyLinkedList.insertNode(self.list, newNode, atIndex=1)

    def test_SinglyLinkedListInsert(self):
        node0 = ADL_SinglyLinkedList(0)
        node1 = ADL_SinglyLinkedList(1)
        node2 = ADL_SinglyLinkedList(2)
        node3 = ADL_SinglyLinkedList(3)
        node4 = ADL_SinglyLinkedList(4)

        self.list = ADL_SinglyLinkedList.insertNode(self.list, node2, atIndex=0)
        self.assertEqual(len(self.list), 1)
        self.assertFalse(ADL_SinglyLinkedList.isEmpty(self.list))
        self.assertEqual(self.list[0].value, 2)
        self.assertTrue(self.list == [2])
        self.assertEqual(self.list, [2])

        self.list = ADL_SinglyLinkedList.insertNode(self.list, node0, atIndex=0)
        self.assertEqual(len(self.list), 2)
        self.assertFalse(ADL_SinglyLinkedList.isEmpty(self.list))
        self.assertEqual(self.list[0].value, 0)
        self.assertTrue(self.list == [0, 2])
        self.assertEqual(self.list, [0, 2])

        listLen = len(self.list)
        self.list = ADL_SinglyLinkedList.insertNode(self.list, node4, atIndex=listLen)
        self.assertEqual(len(self.list), 3)        
        self.assertFalse(ADL_SinglyLinkedList.isEmpty(self.list))
        self.assertEqual(self.list[listLen].value, 4)
        self.assertTrue(self.list == [0, 2, 4])
        self.assertEqual(self.list, [0, 2, 4])

        self.list = ADL_SinglyLinkedList.insertNode(self.list, node1, atIndex=1)
        self.assertEqual(len(self.list), 4)
        self.assertFalse(ADL_SinglyLinkedList.isEmpty(self.list))
        self.assertEqual(self.list[1].value, 1)
        self.assertTrue(self.list == [0, 1, 2, 4])
        self.assertEqual(self.list, [0, 1, 2, 4])

        self.list = ADL_SinglyLinkedList.insertNode(self.list, node3, atIndex=3)
        self.assertEqual(len(self.list), 5)
        self.assertFalse(ADL_SinglyLinkedList.isEmpty(self.list))
        self.assertEqual(self.list[3].value, 3)
        self.assertTrue(self.list == [0, 1, 2, 3, 4])
        self.assertEqual(self.list, [0, 1, 2, 3, 4])

    def test_SinglyLinkedListAppend(self):
        start = 0
        end = 4

        for i in range(start, end+1):
            node = ADL_SinglyLinkedList(i)
            self.list = ADL_SinglyLinkedList.appendNode(self.list, node)
            self.assertEqual(self.list[len(self.list)-1].value, i)
            self.assertEqual(self.list[0].value, start)

    def test_SinglyLinkedListUpdate(self):
        start = 0
        end = 4

        for i in range(start, end+1):
            node = ADL_SinglyLinkedList(i)
            self.list = ADL_SinglyLinkedList.appendNode(self.list, node)

        self.list[0].value = 10
        self.assertEqual(len(self.list), 5)
        self.assertEqual(self.list, [10, 1, 2, 3, 4])
        self.assertEqual(self.list.value, 10)
        self.assertEqual(self.list[0].value, 10)

        self.list[2].value = 12
        self.assertEqual(len(self.list), 5)
        self.assertEqual(self.list, [10, 1, 12, 3, 4])
        self.assertEqual(self.list.value, 10)
        self.assertEqual(self.list[2].value, 12)

        self.list[4].value = 14
        self.assertEqual(len(self.list), 5)
        self.assertEqual(self.list, [10, 1, 12, 3, 14])
        self.assertEqual(self.list.value, 10)
        self.assertEqual(self.list[4].value, 14)

    def test_SinglyLinkedListRemoveOutOfBounds(self):
        with self.assertRaises(AssertionError):
            (self.list, node) = ADL_SinglyLinkedList.removeNode(self.list, atIndex=1)

    def test_SinglyLinkedListRemove(self):
        for i in range(0, 4+1):
            node = ADL_SinglyLinkedList(i)
            self.list = ADL_SinglyLinkedList.appendNode(self.list, node)

        self.assertTrue(self.list == [0,1,2,3,4])

        (self.list, node) = ADL_SinglyLinkedList.removeNode(self.list, atIndex=3)
        self.assertFalse(ADL_SinglyLinkedList.isEmpty(self.list))
        self.assertEqual(node.value, 3)
        self.assertTrue(self.list == [0,1,2,4])
        self.assertEqual(len(self.list), 4)
        self.assertEqual(self.list.value, 0)
        self.assertEqual(self.list[len(self.list)-1].value, 4)

        (self.list, node) = ADL_SinglyLinkedList.removeNode(self.list, atIndex=1)
        self.assertFalse(ADL_SinglyLinkedList.isEmpty(self.list))
        self.assertEqual(node.value, 1)
        self.assertTrue(self.list == [0,2,4])
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list.value, 0)
        self.assertEqual(self.list[len(self.list)-1].value, 4)

        (self.list, node) = ADL_SinglyLinkedList.removeNode(self.list, atIndex=len(self.list)-1)
        self.assertFalse(ADL_SinglyLinkedList.isEmpty(self.list))
        self.assertEqual(node.value, 4)
        self.assertTrue(self.list == [0,2])
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list.value, 0)
        self.assertEqual(self.list[len(self.list)-1].value, 2)

        (self.list, node) = ADL_SinglyLinkedList.removeNode(self.list, atIndex=0)
        self.assertFalse(ADL_SinglyLinkedList.isEmpty(self.list))
        self.assertEqual(node.value, 0)
        self.assertTrue(self.list == [2])
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.value, 2)
        self.assertEqual(self.list[len(self.list)-1].value, 2)

        (self.list, node) = ADL_SinglyLinkedList.removeNode(self.list, atIndex=0)
        self.assertTrue(ADL_SinglyLinkedList.isEmpty(self.list))
        self.assertEqual(node.value, 2)
        self.assertTrue(self.list == None)
        self.assertEqual(ADL_SinglyLinkedList.len(self.list), 0)


    def test_SinglyLinkedListIterator(self):
        for i in range(5):
            node = ADL_SinglyLinkedList(i)
            self.list = ADL_SinglyLinkedList.appendNode(self.list, node)

        for k,v in enumerate(self.list):
            self.assertEqual(k, v)


if __name__ == '__main__':
    unittest.main()